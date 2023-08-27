"""
@Time : 2023/08/22 22:17
@Author : xli_0b101010
@File : batch_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import os

import deepchem as dc
import pandas as pd
from rdkit.Chem import MACCSkeys, MolFromSmiles, MolToSmiles, SDMolSupplier
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QCheckBox, QFileDialog, QHeaderView, QVBoxLayout, QWidget

from utils.functions import *
from utils.load_models import *
from widgets.Ui_batch_page_content import Ui_batchPageContent
from widgets.collapsible_box import CollapsibleBox
from widgets.msg_boxes import *


class batchPageContent(QWidget, Ui_batchPageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        # 初始化状态
        self.txt_data = None
        self.sdf_data = None
        self.file_type = None

        self.batch_start_btn.clicked.connect(self.start_prediction)

        self.predict_methods = {
            'CYP1A2 Inhibition': self.predict_1a2_inhib,
            'CYP2B6 Inhibition': self.predict_2b6_inhib,
            'CYP2C8 Inhibition': self.predict_2c8_inhib,
            'CYP2C9 Inhibition': self.predict_2c9_inhib,
            'CYP2C19 Inhibition': self.predict_2c19_inhib,
            'CYP2D6 Inhibition': self.predict_2d6_inhib,
            'CYP3A4 Inhibition': self.predict_3a4_inhib
        }

        self.isoform_to_column = {
            'CYP1A2 Inhibition': 1,
            'CYP2B6 Inhibition': 3,
            'CYP2C8 Inhibition': 5,
            'CYP2C9 Inhibition': 7,
            'CYP2C19 Inhibition': 9,
            'CYP2D6 Inhibition': 11,
            'CYP3A4 Inhibition': 13
        }

        self.result_model = QStandardItemModel(self)
        headers = (
            'SMILES',
            'CYP1A2\nInhibition', 'CYP1A2\nAD',
            'CYP2B6\nInhibition', 'CYP2B6\nAD',
            'CYP2C8\nInhibition', 'CYP2C8\nAD',
            'CYP2C9\nInhibition', 'CYP2C9\nAD',
            'CYP2C19\nInhibition', 'CYP2C19\nAD',
            'CYP2D6\nInhibition', 'CYP2D6\nAD',
            'CYP3A4\nInhibition', 'CYP3A4\nAD'
        )
        self.result_model.setHorizontalHeaderLabels(headers)
        self.result_model.setColumnCount(len(headers))
        self.batch_table.setModel(self.result_model)

        self.batch_table.setSortingEnabled(True)
        self.batch_table.setAlternatingRowColors(True)

        column_widths = [385, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80, 110, 80]
        for i, width in enumerate(column_widths):
            self.batch_table.setColumnWidth(i, width)

        self.batch_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed
        )
        self.batch_table.verticalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

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
                self.file_type = 'txt'  # 添加一个新属性以分类处理
            elif file_name.endswith('.sdf'):
                with open(file_path, 'r') as f:
                    self.sdf_data = f.read()
                self.file_type = 'sdf'
            else:
                show_file_warning_msgbox(self, self.batch_input_lineEdit)
                self.batch_input_lineEdit.clear()
    
    @Slot()
    def start_prediction(self):
        self.batch_start_btn.setEnabled(False)
        self.batch_input_lineEdit.setEnabled(False)
        self.batch_browse_btn.setEnabled(False)

        self.results_dict = {}

        selected_isoforms = [
            isoform for isoform, cbox in self.cboxes.items() if cbox.isChecked()
        ]

        if not selected_isoforms:
            show_select_warning_msgbox(self, self.batch_input_lineEdit)
            self.end_prediction()
        else:
            if self.file_type == 'txt':
                if not self.txt_data:
                    # 上传的文件内容为空
                    file_empty_warning_msgbox(self, self.batch_input_lineEdit)
                    self.batch_input_lineEdit.clear()
                    self.end_prediction()
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
                        self.update_results(smiles, self.results_dict[smiles])
                    self.batch_input_lineEdit.clear()
                    self.end_prediction()
            elif self.file_type == 'sdf':
                if not self.sdf_data:
                    file_empty_warning_msgbox(self, self.batch_input_lineEdit)
                    self.batch_input_lineEdit.clear()
                    self.end_prediction()
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
                        self.update_results(smiles, self.results_dict[smiles])
                    self.batch_input_lineEdit.clear()
                    self.end_prediction()
            else:
                # 没有上传文件，或上传文件的格式不对后输入框被清空
                no_file_chosen_msgbox(self, self.batch_input_lineEdit)
                self.end_prediction()
    
    def end_prediction(self):
        self.txt_data = None
        self.sdf_data = None
        self.file_type = None
        self.results_dict = {} # 重置
        self.batch_start_btn.setEnabled(True)
        self.batch_input_lineEdit.setEnabled(True)
        self.batch_browse_btn.setEnabled(True)
    
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
        pass

    def predict_2b6_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        fp_2b6 = MACCSkeys.GenMACCSKeys(mol)
        x_2b6 = rdkit_numpy_convert(fp_2b6)

        inhib_proba_2b6, x_2b6_scaled = predict_inhib_proba(
            x_2b6, x_train['2b6'], models['2b6']
        )
        ad_2b6 = is_in_applicability_domain(
            x_2b6_scaled[0], x_train_scaled['2b6'], thresholds['2b6']
        )
        final_inhib_proba_2b6 = is_in_training_set(
            cano_smiles, inhib_proba_2b6, train_data['2b6']
        )

        results_dict.setdefault(smiles, {})[self.isoforms[2]] = (final_inhib_proba_2b6, ad_2b6)

    def predict_2c8_inhib(self, smiles, cano_smiles, _mol=None, results_dict=None):
        featurizer = dc.feat.Mol2VecFingerprint()
        x_2c8 = featurizer.featurize(smiles)

        inhib_proba_2c8, x_2c8_scaled = predict_inhib_proba(
            x_2c8, x_train['2c8'], models['2c8']
        )
        ad_2c8 = is_in_applicability_domain(
            x_2c8_scaled[0], x_train_scaled['2c8'], thresholds['2c8']
        )
        final_inhib_proba_2c8 = is_in_training_set(
            cano_smiles, inhib_proba_2c8, train_data['2c8']
        )

        results_dict.setdefault(smiles, {})[self.isoforms[3]] = (final_inhib_proba_2c8, ad_2c8)

    def predict_2c9_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        pass

    def predict_2c19_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        pass

    def predict_2d6_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        pass

    def predict_3a4_inhib(self, smiles, cano_smiles, mol=None, results_dict=None):
        pass

    def update_results(self, smiles, results_of_smiles):
        row = self.result_model.rowCount()

        smiles_item = QStandardItem(smiles)
        smiles_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 0, smiles_item)

        for isoform, (inhib_proba, ad_status) in results_of_smiles.items():
            col_index = self.isoform_to_column[isoform]

            inhib_proba_item = QStandardItem(inhib_proba)
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
                   for i in range(self.result_model.columnCount())]

        data = []
        for row in range(self.result_model.rowCount()):
            row_data = [str(row + 1)]
            for column in range(self.result_model.columnCount()):
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
