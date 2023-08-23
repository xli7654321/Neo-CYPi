"""
@Time : 2023/08/22 22:17
@Author : xli_0b101010
@File : batch_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import os

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QCheckBox, QFileDialog, QVBoxLayout, QWidget

from widgets.Ui_batch_page_content import Ui_batchPageContent
from widgets.collapsible_box import CollapsibleBox


class batchPageContent(QWidget, Ui_batchPageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # collapsible box
        self.batch_collapsible_box = CollapsibleBox()
        self.batch_collapsible_box.setObjectName("batch_collapsible_box")
        
        cbox_layout = QVBoxLayout()
        cbox_layout.setSpacing(10)

        cyp_isoforms = ["All", "CYP1A2", "CYP2B6", "CYP2C8", "CYP2C9", "CYP2C19", "CYP2D6", "CYP3A4"]
        self.cboxes = []

        for isoform in cyp_isoforms:
            cbox = QCheckBox(isoform)
            cbox.setObjectName(f"single_cbox_{isoform.lower()}")
            cbox_layout.addWidget(cbox)
            self.cboxes.append(cbox)

        self.batch_collapsible_box.set_content_layout(cbox_layout)
        self.batch_gridLayout.addWidget(self.batch_collapsible_box, 2, 0, 1, 1)

        self.cboxes[0].stateChanged.connect(self.manage_cboxes_state)

        # upload file
        self.batch_input_btn.clicked.connect(self.upload_file)

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
    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, caption="Choose file", filter='Text Files (*.txt);;SDF Files (*.sdf)'
        )

        if file_path:
            file_name = os.path.basename(file_path)
            self.batch_input_lineEdit.setText(f"{file_name}")

            if file_name.endswith('.txt'):
                with open(file_path, 'r') as f:
                    txt_data = f.read()
                txt_smiles_list = txt_data.split('\n')
                txt_smiles_list_trim = [s.strip() for s in txt_smiles_list]
             # txt_mol_list = [Chem.MolFromSmiles(s) for s in txt_smiles_list_trim]
                print(txt_smiles_list_trim)
            
            if file_name.endswith('.sdf'):
                pass
