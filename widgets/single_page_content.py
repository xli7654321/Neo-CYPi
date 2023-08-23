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
from rdkit import Chem
from rdkit.Chem import MACCSkeys
from sklearn.preprocessing import StandardScaler

from PySide6.QtCore import QTimer, Qt, Slot
from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QWidget
 
from utils.load_models import *
from widgets.Ui_single_page_content import Ui_singlePageContent
from widgets.collapsible_box import CollapsibleBox


class singlePageContent(QWidget, Ui_singlePageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.single_collapsible_box = CollapsibleBox()
        self.single_collapsible_box.setObjectName("single_collapsible_box")
        
        cbox_layout = QVBoxLayout()
        cbox_layout.setSpacing(10)

        cyp_isoforms = ["All", "CYP1A2", "CYP2B6", "CYP2C8", "CYP2C9", "CYP2C19", "CYP2D6", "CYP3A4"]
        self.cboxes = []

        for isoform in cyp_isoforms:
            cbox = QCheckBox(isoform)
            cbox.setObjectName(f"single_cbox_{isoform.lower()}")
            cbox_layout.addWidget(cbox)
            self.cboxes.append(cbox)

        self.single_collapsible_box.set_content_layout(cbox_layout)
        self.single_gridLayout.addWidget(self.single_collapsible_box, 2, 0, 1, 1)

        self.cboxes[0].stateChanged.connect(self.manage_cboxes_state)

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
        self.single_input_lineEdit.clear()

        # 模拟一个耗时任务
        QTimer.singleShot(5000, self.enable_submit)

    @Slot()
    def enable_submit(self):
        self.single_start_btn.setEnabled(True)
        self.single_input_lineEdit.setEnabled(True)
        self.single_example_btn.setEnabled(True)

    @Slot()
    def single_prediction(self):
        pass
        
        