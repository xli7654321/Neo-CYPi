import deepchem as dc
import pandas as pd
from rdkit.Chem import AllChem, MACCSkeys, MolFromSmiles, MolToSmiles, Draw
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Qt, Slot, Signal
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel, QPixmap, QImage
from PySide6.QtWidgets import (QCheckBox, QFileDialog, QHeaderView, QMessageBox, QVBoxLayout, 
                              QWidget, QDialog, QLabel, QTableView, QStyledItemDelegate, QStyle)
from utils.functions import *
from utils.load_models import *
from ui.Ui_single_page import Ui_singlePage
from widgets.collapsible_box import CollapsibleBox

def smi_to_qpixmap(smi, size=(100, 100), high_res=False):
    mol = MolFromSmiles(smi)
    if mol is None:
        return QPixmap()
    
    # Enlarged high-resolution version
    if high_res:
        draw_size = (size[0], size[1])
        line_width = 2
        font_size = 0.6
    else:
        # Low-resolution version for table display
        draw_size = (size[0] * 2, size[1] * 2)
        line_width = 2
        font_size = 0.6
    
    drawer = Draw.MolDraw2DCairo(draw_size[0], draw_size[1])
    drawer.drawOptions().bondLineWidth = line_width
    drawer.drawOptions().multipleBondOffset = 0.2
    drawer.drawOptions().baseFontSize = font_size
    
    Draw.rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    
    img_data = drawer.GetDrawingText()
    img = QImage.fromData(img_data, 'PNG')
    
    if not high_res:
        img = img.scaled(size[0], size[1], 
                        Qt.AspectRatioMode.KeepAspectRatio, 
                        Qt.TransformationMode.SmoothTransformation)
    
    return QPixmap.fromImage(img)

def smi_to_high_res_qpixmap(smi, size=(400, 400)):
    return smi_to_qpixmap(smi, size, high_res=True)

class ImageDelegate(QStyledItemDelegate):
    """Custom delegate for centering images in table cells"""
    def paint(self, painter, option, index):
        if index.column() == 1:  # image column
            pixmap = index.data(Qt.ItemDataRole.DecorationRole)
            if isinstance(pixmap, QPixmap) and not pixmap.isNull():
                rect = option.rect
                pixmap_rect = pixmap.rect()
                x = rect.x() + (rect.width() - pixmap_rect.width()) // 2
                y = rect.y() + (rect.height() - pixmap_rect.height()) // 2
                
                if option.state & QStyle.State_Selected:
                    painter.fillRect(option.rect, option.palette.highlight())
                else:
                    painter.fillRect(option.rect, option.palette.base())
                
                # Use smooth transformation to draw the image for better display quality
                painter.setRenderHint(painter.RenderHint.Antialiasing, True)
                painter.setRenderHint(painter.RenderHint.SmoothPixmapTransform, True)
                painter.drawPixmap(x, y, pixmap)
                return
        
        super().paint(painter, option, index)

class ImageZoomDialog(QDialog):
    def __init__(self, smiles, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Molecular Image')
        self.setModal(True)
        self.setFixedSize(500, 500)
        
        high_res_pixmap = smi_to_high_res_qpixmap(MolToSmiles(MolFromSmiles(smiles)), size=(450, 450))
        
        label = QLabel()
        label.setPixmap(high_res_pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet('background-color: white; border: 1px solid #ccc;')
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(label)
        self.setLayout(layout)

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

class SinglePage(QWidget, Ui_singlePage):
    show_warning_msgbox_signal = Signal(str, str, str, QWidget)
    start_loading = Signal()
    finish_loading = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show_warning_msgbox_signal.connect(self.show_warning_msgbox)

        # collapsible box
        self.single_collapsible_box = CollapsibleBox()
        self.single_collapsible_box.setObjectName('single_collapsible_box')

        cbox_layout = QVBoxLayout()
        cbox_layout.setSpacing(10)

        self.isoforms = cyp_isoforms
        self.cboxes = {}

        for isoform in self.isoforms:
            cbox = QCheckBox(isoform)
            cbox.setObjectName(f"single_cbox_{isoform.lower()}")
            cbox_layout.addWidget(cbox)
            self.cboxes[isoform] = cbox

        self.single_collapsible_box.set_content_layout(cbox_layout)
        self.single_gridLayout.addWidget(self.single_collapsible_box, 2, 0, 1, 1)

        # get "All" checkbox and other checkboxes
        self.cbox_all = self.cboxes['All']
        self.cboxes_exclude_all = [
            cbox for isoform, cbox in self.cboxes.items() if isoform != 'All'
        ]

        # set "All" checkbox to be checked by default and disable other checkboxes
        self.cbox_all.setChecked(True)
        for cbox in self.cboxes_exclude_all:
            cbox.setDisabled(True)

        # connect "All" checkbox to manage_cboxes_state
        self.cbox_all.stateChanged.connect(self.manage_cboxes_state)

        # Add Enter key event to the start button
        self.single_start_btn.setShortcut(Qt.Key.Key_Return)

        # show example SMILES string
        self.single_example_btn.clicked.connect(self.show_example)

        # start prediction
        self.single_start_btn.clicked.connect(self.start_prediction)

        # init predict methods
        self.predict_methods = {
            'CYP1A2': self.predict_1a2_inhib,
            'CYP2B6': self.predict_2b6_inhib,
            'CYP2C8': self.predict_2c8_inhib,
            'CYP2C9': self.predict_2c9_inhib,
            'CYP2C19': self.predict_2c19_inhib,
            'CYP2D6': self.predict_2d6_inhib,
            'CYP3A4': self.predict_3a4_inhib
        }

        # tableview model
        self.result_model = QStandardItemModel(self)
        headers = ('SMILES', 'Image', 'CYP\nIsoforms', 'Inhibition\nProbability', 'Applicability\nDomain')
        self.result_model.setHorizontalHeaderLabels(headers)
        self.result_model.setColumnCount(len(headers))
        
        if hasattr(self, 'single_table'):
            self.image_delegate = ImageDelegate()
            self.single_table.setItemDelegate(self.image_delegate)
            
            # Disable editing
            self.single_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
            
            original_double_click = self.single_table.mouseDoubleClickEvent
            
            def custom_double_click_event(event):
                index = self.single_table.indexAt(event.pos())
                if index.isValid() and index.column() == 1:
                    smiles_index = self.result_model.index(index.row(), 0)
                    smiles = self.result_model.data(smiles_index, Qt.ItemDataRole.DisplayRole)
                    
                    if smiles:
                        dialog = ImageZoomDialog(smiles, self)
                        dialog.exec()
                        return
                
                original_double_click(event)
            
            self.single_table.mouseDoubleClickEvent = custom_double_click_event
        
        self.single_table.setModel(self.result_model)

        self.single_table.setSortingEnabled(True)
        self.single_table.sortByColumn(3, Qt.SortOrder.DescendingOrder)
        self.single_table.setAlternatingRowColors(True)
        
        # Fix the width of the last four columns
        column_widths = [125, 100, 100, 100]
        for i, width in enumerate(column_widths, start=1):
            self.single_table.setColumnWidth(i, width)

        # tableview horizontal header
        self.single_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )
        
        # tableview vertical header
        self.single_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed
        )
        self.single_table.verticalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.single_table.verticalHeader().setDefaultSectionSize(120)

        self.single_clear_btn.clicked.connect(self.clear_results)
        self.single_save_btn.clicked.connect(self.save_results)

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
    def show_example(self):
        self.single_input_lineEdit.setText(
            self.single_input_lineEdit.placeholderText()
        )

    @Slot()
    def start_prediction(self):
        # disable start btn, input lineEdit and example btn after starting prediction
        self.single_start_btn.setEnabled(False)
        self.single_input_lineEdit.setEnabled(False)
        self.single_example_btn.setEnabled(False)
        self.start_loading.emit()

        worker = PredictionWorker(self._run_prediction)
        worker.signals.finished.connect(self.end_prediction)
        QThreadPool.globalInstance().setMaxThreadCount(8)
        QThreadPool.globalInstance().start(worker)

    def _run_prediction(self):
        selected_isoforms = [
            isoform for isoform, cbox in self.cboxes.items() if cbox.isChecked()
        ]
        if not selected_isoforms:
            self.show_warning_msgbox_signal.emit(
                'Select Error', 
                'No Model Selected!', 
                'Please select at least one model to start prediction.', 
                self.single_input_lineEdit
            )
            return
        else:
            smiles = self.single_input_lineEdit.text().strip()
            if not smiles:
                # empty input
                self.show_warning_msgbox_signal.emit(
                    'Input Error', 
                    'Please input a valid SMILES string!', 
                    None, 
                    self.single_input_lineEdit
                )
                return
            else:
                mol = MolFromSmiles(smiles)
                if mol is None:
                    self.show_warning_msgbox_signal.emit(
                        'Input Error', 
                        'Please input a valid SMILES string!', 
                        None, 
                        self.single_input_lineEdit
                    )
                    return
                else:
                    # canonicalize input SMILES string
                    cano_smiles = MolToSmiles(mol)
                    if 'All' in selected_isoforms:
                        self.predict_all(smiles, cano_smiles, mol)
                        self.single_input_lineEdit.clear()
                        return
                    else:
                        for isoform in selected_isoforms:
                            if isoform in self.predict_methods.keys():
                                self.predict_methods[isoform](smiles, cano_smiles, mol)
                        self.single_input_lineEdit.clear()
                        return

    @Slot()
    def end_prediction(self):
        self.single_start_btn.setEnabled(True)
        self.single_input_lineEdit.setEnabled(True)
        self.single_example_btn.setEnabled(True)
        self.finish_loading.emit()
    
    def predict_all(self, smiles, cano_smiles, mol):
        for method in self.predict_methods.values():
            method(smiles, cano_smiles, mol)

    # predict method for each isoform
    def predict_1a2_inhib(self, smiles, cano_smiles, mol=None):
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
        
        self.update_results(
            smiles, cano_smiles, self.isoforms[1], final_inhib_proba_1a2, ad_1a2
        )
    
    def predict_2b6_inhib(self, smiles, cano_smiles, mol=None):
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

        self.update_results(
            smiles, cano_smiles, self.isoforms[2], final_inhib_proba_2b6, ad_2b6
        )

    def predict_2c8_inhib(self, smiles, cano_smiles, _mol=None):
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

        self.update_results(
            smiles, cano_smiles, self.isoforms[3], final_inhib_proba_2c8, ad_2c8
        )

    def predict_2c9_inhib(self, smiles, cano_smiles, mol=None):
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
        
        self.update_results(
            smiles, cano_smiles, self.isoforms[4], final_inhib_proba_2c9, ad_2c9
        )

    def predict_2c19_inhib(self, smiles, cano_smiles, mol=None):
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
        
        self.update_results(
            smiles, cano_smiles, self.isoforms[5], final_inhib_proba_2c19, ad_2c19
        )

    def predict_2d6_inhib(self, smiles, cano_smiles, mol=None):
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
        
        self.update_results(
            smiles, cano_smiles, self.isoforms[6], final_inhib_proba_2d6, ad_2d6
        )

    def predict_3a4_inhib(self, smiles, cano_smiles, mol=None):
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
        
        self.update_results(
            smiles, cano_smiles, self.isoforms[7], final_inhib_proba_3a4, ad_3a4
        )

    def update_results(self, smiles, cano_smiles, model, proba, ad_status):
        row = self.result_model.rowCount()

        smiles_item = QStandardItem(smiles)
        smiles_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 0, smiles_item)
        
        pixmap = smi_to_qpixmap(cano_smiles, size=(100, 100), high_res=False)
        image_item = QStandardItem()
        image_item.setData(pixmap, Qt.ItemDataRole.DecorationRole)
        self.result_model.setItem(row, 1, image_item)
        
        model_item = QStandardItem(model)
        model_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 2, model_item)

        proba_item = QStandardItem(f"{float(proba):.3f}")
        proba_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 3, proba_item)

        ad_item = QStandardItem(ad_status)
        ad_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 4, ad_item)
    
    @Slot()
    def save_results(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, caption='Save File', dir='results.csv', filter='CSV Files (*.csv);;All Files (*)'
        )
        
        if file_path:
            if not file_path.endswith('.csv'):
                file_path += '.csv'
        
        # Extract headers
        headers = [self.result_model.horizontalHeaderItem(i).text() 
                   for i in range(self.result_model.columnCount())
                   if i != 1]
        
        # Extract data
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
        
        # Convert to DataFrame
        df = pd.DataFrame(data, columns=['Index'] + headers)
        
        # Save to CSV
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
            # After the user clicks OK, set the focus back to the input widget
            input_widget.setFocus()
            return