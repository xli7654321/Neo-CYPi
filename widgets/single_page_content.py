"""
@Time : 2023/08/18 01:52
@Author : xli_0b101010
@File : single_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import deepchem as dc
import numpy as np
import pandas as pd
from rdkit.Chem import MACCSkeys, MolFromSmiles, MolToSmiles

from PySide6.QtCore import QTimer, Qt, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QWidget

from utils.functions import *
from utils.load_models import *
from widgets.Ui_single_page_content import Ui_singlePageContent
from widgets.collapsible_box import CollapsibleBox
from widgets.msg_boxes import *


class singlePageContent(QWidget, Ui_singlePageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # add a collapsible box
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
        self.cboxes_exclude_all = [cbox for isoform, cbox in self.cboxes.items() if isoform != 'All']

        # set "All" checkbox to be checked by default and disable other checkboxes
        self.cbox_all.setChecked(True)
        for cbox in self.cboxes_exclude_all:
            cbox.setDisabled(True)

        # connect "All" checkbox to manage_cboxes_state
        self.cbox_all.stateChanged.connect(self.manage_cboxes_state)

        # 给 start 按钮添加回车事件
        self.single_start_btn.setShortcut(Qt.Key.Key_Return)

        # show example SMILES string
        self.single_example_btn.clicked.connect(self.show_example)

        # start prediction
        self.single_start_btn.clicked.connect(self.start_prediction)

        # init predict methods
        self.predict_methods = {
            'CYP2B6 Inhibition': predict_2b6_inhib,
            'CYP2C8 Inhibition': predict_2c8_inhib
        }

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
        self.single_input_lineEdit.setText(self.single_input_lineEdit.placeholderText())

    @Slot()
    def start_prediction(self):
        # disable start button, input lineEdit and example button after starting prediction
        self.single_start_btn.setEnabled(False)
        self.single_input_lineEdit.setEnabled(False)
        self.single_example_btn.setEnabled(False)

        smiles = self.single_input_lineEdit.text().strip()
        if not smiles:
            # 输入为空
            show_input_warning_msgbox(self, self.single_input_lineEdit)
            self.end_prediction()
        else:
            # 输入不合法，无法生成 mol 对象
            mol = MolFromSmiles(smiles)
            if mol is None:
                show_input_warning_msgbox(self, self.single_input_lineEdit)
                self.end_prediction()
            else:
                # canonicalize input SMILES string
                cano_smiles = MolToSmiles(mol)

                selected_isoforms = [isoform for isoform, cbox in self.cboxes.items() if cbox.isChecked()]
                print(selected_isoforms)

                if not selected_isoforms:
                    show_select_warning_msgbox(self, self.single_input_lineEdit)
                    self.end_prediction()
                elif 'All' in selected_isoforms:
                    self.single_input_lineEdit.clear()
                    self.predict_all(smiles, cano_smiles, mol)
                    self.end_prediction()
                else:
                    self.single_input_lineEdit.clear()
                    for isoform in selected_isoforms:
                        if isoform in self.predict_methods.keys():
                            self.predict_methods[isoform](smiles, cano_smiles, mol)
                    self.end_prediction()

    def predict_all(self, smiles, cano_smiles, mol):
        for method in self.predict_methods.values():
            method(smiles, cano_smiles, mol)

    def end_prediction(self):
        self.single_start_btn.setEnabled(True)
        self.single_input_lineEdit.setEnabled(True)
        self.single_example_btn.setEnabled(True)


# predict method for each isoform
def predict_2b6_inhib(smiles, cano_smiles, mol=None):
    if mol is None:
        mol = MolFromSmiles(smiles)

    # 分子表征
    fp_2b6 = MACCSkeys.GenMACCSKeys(mol)
    x_2b6 = rdkit_numpy_convert(fp_2b6)

    # 预测抑制概率
    inhib_proba_2b6, x_2b6_scaled = predict_inhib_proba(
        x_2b6, x_train['2b6'], models['2b6']
    )

    # 判断分子是否在预测模型的应用域内
    ad_2b6 = is_in_applicability_domain(
        x_2b6_scaled[0], x_train_scaled['2b6'], thresholds['2b6']
    )

    # 判断分子是否在预测模型的训练集中
    final_inhib_proba_2b6 = is_in_training_set(
        cano_smiles, inhib_proba_2b6, train_data['2b6']
    )

    print(final_inhib_proba_2b6, ad_2b6)
    # return final_inhib_proba_2b6, ad_2b6


def predict_2c8_inhib(smiles, cano_smiles, _mol=None):
    featurizer = dc.feat.Mol2VecFingerprint()
    x_2c8 = featurizer.featurize(smiles)

    inhib_proba_2c8, x_2c8_scaled = predict_inhib_proba(
        x_2c8, x_train['2c8'], models['2c8']
    )

    ad_2c8 = is_in_applicability_domain(
        x_2c8_scaled[0], x_train_scaled['2c8'], thresholds['2c8']
    )

    final_inhib_proba_2c8 = is_in_training_set(
        cano_smiles, inhib_proba_2c8, train_data['2b6']
    )

    print(final_inhib_proba_2c8, ad_2c8)
    # return final_inhib_proba_2c8, ad_2c8
