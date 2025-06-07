import os
import deepchem as dc
import pandas as pd
from rdkit.Chem import AllChem, MACCSkeys, MolFromSmiles, MolToSmiles, SDMolSupplier
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Qt, Slot, Signal
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel, QPixmap, QImage
from PySide6.QtWidgets import (QCheckBox, QFileDialog, QHeaderView, QMessageBox, QVBoxLayout, 
                              QWidget, QDialog, QLabel, QTableView, QStyledItemDelegate, QStyle)
from utils.functions import *
from utils.load_models import *
from ui.Ui_batch_page import Ui_batchPage
from widgets.collapsible_box import CollapsibleBox
from widgets.single_page import smi_to_qpixmap, ImageDelegate, ImageZoomDialog

class PredictionSignals(QObject):
    finished = Signal()

class PredictionWorker(QRunnable):
    def __init__(self, function):
        super().__init__()
        self.function = function
        self.signals = PredictionSignals()

    def run(self):
        self.function()
        self.signals.finished.emit()

class BatchPage(QWidget, Ui_batchPage):
    show_warning_msgbox_signal = Signal(str, str, str, QWidget)
    start_loading = Signal()
    finish_loading = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show_warning_msgbox_signal.connect(self.show_warning_msgbox)

        self.batch_collapsible_box = CollapsibleBox()
        self.batch_collapsible_box.setObjectName('batch_collapsible_box')
        
        cbox_layout = QVBoxLayout()
        cbox_layout.setSpacing(10)

        self.isoforms = cyp_isoforms
        self.cboxes = {}

        for isoform in self.isoforms:
            cbox = QCheckBox(isoform)
            cbox.setObjectName(f"batch_cbox_{isoform.lower()}")
            cbox_layout.addWidget(cbox)
            self.cboxes[isoform] = cbox

        self.batch_collapsible_box.set_content_layout(cbox_layout)
        self.batch_gridLayout.addWidget(self.batch_collapsible_box, 2, 0, 1, 1)

        self.cbox_all = self.cboxes['All']
        self.cboxes_exclude_all = [
            cbox for isoform, cbox in self.cboxes.items() if isoform != 'All'
        ]

        self.cbox_all.setChecked(True)
        for cbox in self.cboxes_exclude_all:
            cbox.setDisabled(True)

        self.cbox_all.stateChanged.connect(self.manage_cboxes_state)
        
        self.batch_start_btn.setShortcut(Qt.Key.Key_Return)

        # upload file
        self.batch_browse_btn.clicked.connect(self.upload_file)
        
        self.txt_data = None
        self.sdf_data = None
        self.file_type = None

        self.batch_start_btn.clicked.connect(self.start_prediction)

        self.predict_methods = {
            'CYP1A2': self.predict_1a2_inhib,
            'CYP2B6': self.predict_2b6_inhib,
            'CYP2C8': self.predict_2c8_inhib,
            'CYP2C9': self.predict_2c9_inhib,
            'CYP2C19': self.predict_2c19_inhib,
            'CYP2D6': self.predict_2d6_inhib,
            'CYP3A4': self.predict_3a4_inhib
        }

        self.isoform_to_column = {
            'CYP1A2': 2,
            'CYP2B6': 4,
            'CYP2C8': 6,
            'CYP2C9': 8,
            'CYP2C19': 10,
            'CYP2D6': 12,
            'CYP3A4': 14
        }

        self.result_model = QStandardItemModel(self)
        headers = (
            'SMILES', 'Image',
            'CYP1A2', 'CYP1A2\nAD',
            'CYP2B6', 'CYP2B6\nAD',
            'CYP2C8', 'CYP2C8\nAD',
            'CYP2C9', 'CYP2C9\nAD',
            'CYP2C19', 'CYP2C19\nAD',
            'CYP2D6', 'CYP2D6\nAD',
            'CYP3A4', 'CYP3A4\nAD'
        )
        self.result_model.setHorizontalHeaderLabels(headers)
        self.result_model.setColumnCount(len(headers))
        
        if hasattr(self, 'batch_table'):
            self.image_delegate = ImageDelegate()
            self.batch_table.setItemDelegate(self.image_delegate)
            
            # Disable editing
            self.batch_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
            
            original_double_click = self.batch_table.mouseDoubleClickEvent
            
            def custom_double_click_event(event):
                index = self.batch_table.indexAt(event.pos())
                if index.isValid() and index.column() == 1:
                    smiles_index = self.result_model.index(index.row(), 0)
                    smiles = self.result_model.data(smiles_index, Qt.ItemDataRole.DisplayRole)
                    
                    if smiles:
                        dialog = ImageZoomDialog(smiles, self)
                        dialog.exec()
                        return
                
                original_double_click(event)
            
            self.batch_table.mouseDoubleClickEvent = custom_double_click_event
        
        self.batch_table.setModel(self.result_model)
        
        self.batch_table.setSortingEnabled(True)
        self.batch_table.setAlternatingRowColors(True)

        column_widths = [385, 125, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80]
        for i, width in enumerate(column_widths):
            self.batch_table.setColumnWidth(i, width)

        self.batch_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed
        )
        self.batch_table.verticalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.batch_table.verticalHeader().setDefaultSectionSize(120)

        self.batch_clear_btn.clicked.connect(self.clear_results)
        self.batch_save_btn.clicked.connect(self.save_results)

    @Slot()
    def manage_cboxes_state(self):
        """
        If "All" checkbox is checked, disable all other checkboxes
        Otherwise, enable all other checkboxes
        """
        state_cbox_all = self.cbox_all.isChecked()
        for cbox in self.cboxes_exclude_all:
            if cbox.isChecked():
                cbox.setChecked(False)
            cbox.setDisabled(state_cbox_all)

    @Slot()
    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, caption='Choose file', filter='Text Files (*.txt);;SDF Files (*.sdf);;All Files (*)'
        )

        if file_path:
            file_name = os.path.basename(file_path)
            self.batch_input_lineEdit.setText(file_name)

            if file_name.endswith('.txt'):
                with open(file_path, 'r') as f:
                    self.txt_data = f.read()
                self.file_type = 'txt'
            elif file_name.endswith('.sdf'):
                with open(file_path, 'r') as f:
                    self.sdf_data = f.read()
                self.file_type = 'sdf'
            else:
                self.show_warning_msgbox_signal.emit(
                    'File Type Error', 
                    'Invalid File Type!', 
                    'Please upload a valid txt or sdf format file for prediction.', 
                    self.batch_input_lineEdit
                )
                self.batch_input_lineEdit.clear()
    
    @Slot()
    def start_prediction(self):
        self.batch_start_btn.setEnabled(False)
        self.batch_input_lineEdit.setEnabled(False)
        self.batch_browse_btn.setEnabled(False)

        self.start_loading.emit()

        worker = PredictionWorker(self._run_prediction)
        worker.signals.finished.connect(self.end_prediction)
        QThreadPool.globalInstance().setMaxThreadCount(8)
        QThreadPool.globalInstance().start(worker)

    def _run_prediction(self):
        self.results_dict = {}

        selected_isoforms = [
            isoform for isoform, cbox in self.cboxes.items() if cbox.isChecked()
        ]

        if not selected_isoforms:
            self.show_warning_msgbox_signal.emit(
                'Select Error', 
                'No Model Selected!', 
                'Please select at least one model to start prediction.', 
                self.batch_input_lineEdit
            )
            return
        else:
            if self.file_type == 'txt':
                if not self.txt_data:
                    self.show_warning_msgbox_signal.emit(
                        'File Content Error', 
                        'The Uploaded File is Empty!', 
                        'Please check the contents of your file and upload again.', 
                        self.batch_input_lineEdit
                    )
                    self.batch_input_lineEdit.clear()
                    return
                else:
                    txt_smiles_list = [s.strip() for s in self.txt_data.split('\n') if s.strip()]
                    txt_mol_list = [MolFromSmiles(smiles) for smiles in txt_smiles_list]
                    for index, mol in enumerate(txt_mol_list):
                        if mol is None:
                            smiles = txt_smiles_list[index]
                            self.if_mol_is_none(smiles, selected_isoforms, self.results_dict)
                        else:
                            smiles = txt_smiles_list[index]
                            cano_smiles = MolToSmiles(mol)
                            if 'All' in selected_isoforms:
                                selected_isoforms = self.isoforms[1:]
                                self.predict_all(smiles, cano_smiles, mol, self.results_dict)
                            else:
                                for isoform in selected_isoforms:
                                    if isoform in self.predict_methods.keys():
                                        self.predict_methods[isoform](smiles, cano_smiles, mol, self.results_dict)
                        self.update_results(smiles, cano_smiles, self.results_dict[smiles])
                    self.batch_input_lineEdit.clear()
                    return
            elif self.file_type == 'sdf':
                if not self.sdf_data:
                    self.show_warning_msgbox_signal.emit(
                        'File Content Error', 
                        'The Uploaded File is Empty!', 
                        'Please check the contents of your file and upload again.', 
                        self.batch_input_lineEdit
                    )
                    self.batch_input_lineEdit.clear()
                    return
                else:
                    suppl = SDMolSupplier()
                    suppl.SetData(self.sdf_data)
                    for index, mol in enumerate(suppl):
                        if mol is None:
                            smiles = 'null'
                            self.if_mol_is_none(smiles, selected_isoforms, self.results_dict)
                        else:
                            smiles = MolToSmiles(mol)
                            cano_smiles = smiles
                            if 'All' in selected_isoforms:
                                selected_isoforms = self.isoforms[1:]
                                self.predict_all(smiles, cano_smiles, mol, self.results_dict)
                            else:
                                for isoform in selected_isoforms:
                                    if isoform in self.predict_methods.keys():
                                        self.predict_methods[isoform](smiles, cano_smiles, mol, self.results_dict)
                        self.update_results(smiles, cano_smiles, self.results_dict[smiles])
                    self.batch_input_lineEdit.clear()
                    return
            else:
                # The input box is cleared when no file is uploaded or the uploaded file format is incorrect
                self.show_warning_msgbox_signal.emit(
                    'File Error', 
                    'No File Chosen!', 
                    'Please choose a file to upload before prediction.', 
                    self.batch_input_lineEdit
                )
                return
    
    @Slot()
    def end_prediction(self):
        self.txt_data = None
        self.sdf_data = None
        self.file_type = None
        self.results_dict = {}

        self.batch_start_btn.setEnabled(True)
        self.batch_input_lineEdit.setEnabled(True)
        self.batch_browse_btn.setEnabled(True)
        
        self.finish_loading.emit()
    
    def predict_all(self, smiles, cano_smiles, mol, results_dict):
        for method in self.predict_methods.values():
            method(smiles, cano_smiles, mol, results_dict)

    def if_mol_is_none(self, smiles, selected_isoforms, results_dict):
        results_of_none = {}
        inhib_proba = 'null'
        ad_status = 'null'
        for isoform in selected_isoforms:
            results_of_none[isoform] = (inhib_proba, ad_status)
        results_dict[smiles] = results_of_none

    def predict_1a2_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        fp_1a2 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
        x_1a2 = rdkit_numpy_convert(fp_1a2)
        fp_train_1a2 = [AllChem.GetMorganFingerprintAsBitVect(MolFromSmiles(s), 2)
                        for s in train_data['1a2']['SMILES']]
        
        inhib_proba_1a2 = predict_inhib_proba_l(
            x_1a2, models['1a2']
        )
        final_inhib_proba_1a2 = is_in_training_set(
            cano_smiles, inhib_proba_1a2, train_data['1a2']
        )
        ad_1a2 = is_in_domain_tanimoto(fp_1a2, fp_train_1a2, thresholds['1a2'])
        
        results_dict.setdefault(smiles, {})[self.isoforms[1]] = (final_inhib_proba_1a2, ad_1a2)

    def predict_2b6_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        fp_2b6 = MACCSkeys.GenMACCSKeys(mol)
        x_2b6 = rdkit_numpy_convert(fp_2b6)

        inhib_proba_2b6, x_2b6_scaled = predict_inhib_proba_s(
            x_2b6, x_train['2b6'], models['2b6']
        )
        final_inhib_proba_2b6 = is_in_training_set(
            cano_smiles, inhib_proba_2b6, train_data['2b6']
        )
        ad_2b6 = is_in_applicability_domain(
            x_2b6_scaled[0], x_train_scaled['2b6'], thresholds['2b6']
        )

        results_dict.setdefault(smiles, {})[self.isoforms[2]] = (final_inhib_proba_2b6, ad_2b6)

    def predict_2c8_inhib(self, smiles, cano_smiles, _mol=None, results_dict=None):
        featurizer = dc.feat.Mol2VecFingerprint()
        x_2c8 = featurizer.featurize(smiles)

        inhib_proba_2c8, x_2c8_scaled = predict_inhib_proba_s(
            x_2c8, x_train['2c8'], models['2c8']
        )
        final_inhib_proba_2c8 = is_in_training_set(
            cano_smiles, inhib_proba_2c8, train_data['2c8']
        )
        ad_2c8 = is_in_applicability_domain(
            x_2c8_scaled[0], x_train_scaled['2c8'], thresholds['2c8']
        )

        results_dict.setdefault(smiles, {})[self.isoforms[3]] = (final_inhib_proba_2c8, ad_2c8)

    def predict_2c9_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        featurizer = dc.feat.Mol2VecFingerprint()
        x_2c9 = featurizer.featurize(smiles)
        
        fp_2c9 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
        fp_train_2c9 = [AllChem.GetMorganFingerprintAsBitVect(MolFromSmiles(s), 2)
                        for s in train_data['2c9']['SMILES']]
        
        inhib_proba_2c9 = predict_inhib_proba_l(
            x_2c9, models['2c9']
        )
        final_inhib_proba_2c9 = is_in_training_set(
            cano_smiles, inhib_proba_2c9, train_data['2c9']
        )
        ad_2c9 = is_in_domain_tanimoto(fp_2c9, fp_train_2c9, thresholds['2c9'])

        results_dict.setdefault(smiles, {})[self.isoforms[4]] = (final_inhib_proba_2c9, ad_2c9)

    def predict_2c19_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        featurizer = dc.feat.Mol2VecFingerprint()
        x_2c19 = featurizer.featurize(smiles)
        
        fp_2c19 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
        fp_train_2c19 = [AllChem.GetMorganFingerprintAsBitVect(MolFromSmiles(s), 2)
                         for s in train_data['2c19']['SMILES']]
        
        inhib_proba_2c19 = predict_inhib_proba_l(
            x_2c19, models['2c19']
        )
        final_inhib_proba_2c19 = is_in_training_set(
            cano_smiles, inhib_proba_2c19, train_data['2c19']
        )
        ad_2c19 = is_in_domain_tanimoto(fp_2c19, fp_train_2c19, thresholds['2c19'])
        
        results_dict.setdefault(smiles, {})[self.isoforms[5]] = (final_inhib_proba_2c19, ad_2c19)

    def predict_2d6_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        fp_2d6 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
        x_2d6 = rdkit_numpy_convert(fp_2d6)
        fp_train_2d6 = [AllChem.GetMorganFingerprintAsBitVect(MolFromSmiles(s), 2)
                        for s in train_data['2d6']['SMILES']]
        
        inhib_proba_2d6 = predict_inhib_proba_l(
            x_2d6, models['2d6']
        )
        final_inhib_proba_2d6 = is_in_training_set(
            cano_smiles, inhib_proba_2d6, train_data['2d6']
        )
        ad_2d6 = is_in_domain_tanimoto(fp_2d6, fp_train_2d6, thresholds['2d6'])
        
        results_dict.setdefault(smiles, {})[self.isoforms[6]] = (final_inhib_proba_2d6, ad_2d6)

    def predict_3a4_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        featurizer = dc.feat.Mol2VecFingerprint()
        x_3a4 = featurizer.featurize(smiles)
        
        fp_3a4 = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
        fp_train_3a4 = [AllChem.GetMorganFingerprintAsBitVect(MolFromSmiles(s), 2)
                        for s in train_data['3a4']['SMILES']]
        
        inhib_proba_3a4 = predict_inhib_proba_l(
            x_3a4, models['3a4']
        )
        final_inhib_proba_3a4 = is_in_training_set(
            cano_smiles, inhib_proba_3a4, train_data['3a4']
        )
        ad_3a4 = is_in_domain_tanimoto(fp_3a4, fp_train_3a4, thresholds['3a4'])
        
        results_dict.setdefault(smiles, {})[self.isoforms[7]] = (final_inhib_proba_3a4, ad_3a4)

    def update_results(self, smiles, cano_smiles, results_of_smiles):
        row = self.result_model.rowCount()

        smiles_item = QStandardItem(smiles)
        smiles_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 0, smiles_item)
        
        pixmap = smi_to_qpixmap(cano_smiles, size=(100, 100), high_res=False)
        image_item = QStandardItem()
        image_item.setData(pixmap, Qt.ItemDataRole.DecorationRole)
        self.result_model.setItem(row, 1, image_item)

        for isoform, (inhib_proba, ad_status) in results_of_smiles.items():
            col_index = self.isoform_to_column[isoform]

            inhib_proba_item = QStandardItem(f"{float(inhib_proba):.3f}")
            inhib_proba_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.result_model.setItem(row, col_index, inhib_proba_item)

            ad_item = QStandardItem(ad_status)
            ad_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.result_model.setItem(row, col_index + 1, ad_item)
    
    @Slot()
    def save_results(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, caption='Save File', dir='results.csv', filter='CSV Files (*.csv);;All Files (*)'
        )
        
        if file_path:
            if not file_path.endswith('.csv'):
                file_path += '.csv'

        headers = [self.result_model.horizontalHeaderItem(i).text() 
                   for i in range(self.result_model.columnCount())
                   if i != 1]

        data = []
        for row in range(self.result_model.rowCount()):
            row_data = [str(row + 1)]
            for column in range(self.result_model.columnCount()):
                if column == 1:
                    continue
                item = self.result_model.item(row, column)
                if item and item.text():
                    row_data.append(item.text())
                else:
                    row_data.append('')
            data.append(row_data)
        
        df = pd.DataFrame(data, columns=['Index'] + headers)
        df.to_csv(file_path, index=False)

    @Slot()
    def clear_results(self):
        self.result_model.removeRows(0, self.result_model.rowCount())

    @Slot(str, str, str, QWidget)
    def show_warning_msgbox(self, title, text, informative_text, input_widget):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setInformativeText(informative_text)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setFont(QFont('Segoe UI', 11))
    
        reply = msg_box.exec()
    
        if reply == QMessageBox.StandardButton.Ok:
            input_widget.setFocus()
            return
