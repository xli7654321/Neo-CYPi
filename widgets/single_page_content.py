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
from widgets.msg_boxes import show_input_warning_msgbox


class singlePageContent(QWidget, Ui_singlePageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.single_collapsible_box = CollapsibleBox()
        self.single_collapsible_box.setObjectName("single_collapsible_box")
        
        cbox_layout = QVBoxLayout()
        cbox_layout.setSpacing(10)

        self.isoforms = cyp_isoforms
        self.cboxes = []

        for isoform in self.isoforms:
            cbox = QCheckBox(isoform)
            cbox.setObjectName(f"single_cbox_{isoform.lower()}")
            cbox_layout.addWidget(cbox)
            self.cboxes.append(cbox)

        self.single_collapsible_box.set_content_layout(cbox_layout)
        self.single_gridLayout.addWidget(self.single_collapsible_box, 2, 0, 1, 1)

        self.cboxes[0].stateChanged.connect(self.manage_cboxes_state)

        # 给 start 按钮添加回车事件
        self.single_start_btn.setShortcut(Qt.Key.Key_Return)

        # show example SMILES string
        self.single_example_btn.clicked.connect(self.show_example)

        # get input SMILES string
        self.single_start_btn.clicked.connect(self.get_input_smiles)
        # start prediction
        self.single_start_btn.clicked.connect(self.single_prediction)
        

    @Slot()
    def manage_cboxes_state(self):
        """
        If "All" checkbox is checked, disable all other checkboxes
        Otherwise, enable all other checkboxes
        """
        cbox_all_state = self.cboxes[0].isChecked()
        for cbox in self.cboxes[1:]:
            if cbox.isChecked():
                cbox.setChecked(False)
            cbox.setDisabled(cbox_all_state)
        
    @Slot()
    def show_example(self):
        self.single_input_lineEdit.setText(self.single_input_lineEdit.placeholderText())

    @Slot()
    def get_input_smiles(self):
        self.single_start_btn.setEnabled(False)
        self.single_input_lineEdit.setEnabled(False)
        self.single_example_btn.setEnabled(False)

        self.input_smiles = self.single_input_lineEdit.text()

        # 模拟一个耗时任务
        QTimer.singleShot(5000, self.enable_submit)

    @Slot()
    def enable_submit(self):
        self.single_start_btn.setEnabled(True)
        self.single_input_lineEdit.setEnabled(True)
        self.single_example_btn.setEnabled(True)

    @Slot()
    def single_prediction(self):
        smiles = self.input_smiles.strip()
        if not smiles:
            # 输入为空
            show_input_warning_msgbox(self, self.single_input_lineEdit)
        else:
            # 输入不合法，无法生成 mol 对象
            mol = MolFromSmiles(smiles)
            if mol is None:
                show_input_warning_msgbox(self, self.single_input_lineEdit)
            else:
                # 输入合法，清空输入框
                self.single_input_lineEdit.clear()

                # 分子表征
                fp_2b6 = MACCSkeys.GenMACCSKeys(mol)
                x_2b6 = rdkit_numpy_convert(fp_2b6)

                featurizer = dc.feat.Mol2VecFingerprint()
                x_2c8 = featurizer.featurize(smiles)

                # 预测抑制概率
                inhibition_proba_str_2b6, x_2b6_scaled = predict_inhibition_proba(
                    x_2b6, x_train['2b6'], models['2b6']
                )
                inhibition_proba_str_2c8, x_2c8_scaled = predict_inhibition_proba(
                    x_2c8, x_train['2c8'], models['2c8']
                )

                # 判断分子是否在预测模型的应用域内
                ad_2b6 = is_in_applicability_domain(
                    x_2b6_scaled[0], x_train_scaled['2b6'], thresholds['2b6']
                )
                ad_2c8 = is_in_applicability_domain(
                    x_2c8_scaled[0], x_train_scaled['2c8'], thresholds['2c8']
                )

                # 判断分子是否在预测模型的训练集中
                original_smiles = str(MolToSmiles(mol))
                current_smiles, inhibition_proba_str_2b6 = is_in_training_set(
                    original_smiles, original_smiles, inhibition_proba_str_2b6, train_data['2b6']
                )
                current_smiles, inhibition_proba_str_2c8 = is_in_training_set(
                    original_smiles, current_smiles, inhibition_proba_str_2c8, train_data['2c8']
                )
