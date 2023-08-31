"""
@Time : 2023/08/18 01:52
@Author : xli_0b101010
@File : single_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import deepchem as dc
import pandas as pd
from rdkit.Chem import MACCSkeys, MolFromSmiles, MolToSmiles
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Qt, Slot, Signal
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QCheckBox, QFileDialog, QHeaderView, QMessageBox, QVBoxLayout, QWidget

from utils.functions import *
from utils.load_models import *
from widgets.Ui_single_page_content import Ui_singlePageContent
from widgets.collapsible_box import CollapsibleBox


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


class SinglePageContent(QWidget, Ui_singlePageContent):
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

        # 给 start 按钮添加回车事件
        self.single_start_btn.setShortcut(Qt.Key.Key_Return)

        # show example SMILES string
        self.single_example_btn.clicked.connect(self.show_example)

        # start prediction
        self.single_start_btn.clicked.connect(self.start_prediction)

        # init predict methods
        self.predict_methods = {
            'CYP1A2 Inhibition': self.predict_1a2_inhib,
            'CYP2B6 Inhibition': self.predict_2b6_inhib,
            'CYP2C8 Inhibition': self.predict_2c8_inhib,
            'CYP2C9 Inhibition': self.predict_2c9_inhib,
            'CYP2C19 Inhibition': self.predict_2c19_inhib,
            'CYP2D6 Inhibition': self.predict_2d6_inhib,
            'CYP3A4 Inhibition': self.predict_3a4_inhib
        }

        # tableview model
        self.result_model = QStandardItemModel(self)
        headers = ('SMILES', 'Prediction\nModel', 'Inhibition\nProbability', 'Applicability\nDomain')
        self.result_model.setHorizontalHeaderLabels(headers)
        self.result_model.setColumnCount(len(headers))
        self.single_table.setModel(self.result_model)

        # tableview 整体
        # font set by qss
        self.single_table.setSortingEnabled(True)
        self.single_table.sortByColumn(2, Qt.SortOrder.DescendingOrder)
        self.single_table.setAlternatingRowColors(True)
        
        # 后三列固定宽度
        column_widths = [160, 110, 110]
        for i, width in enumerate(column_widths, start=1):
            self.single_table.setColumnWidth(i, width)

        # tableview 水平标题
        self.single_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )

        # tableview 垂直标题
        self.single_table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed
        )
        self.single_table.verticalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

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
        QThreadPool.globalInstance().setMaxThreadCount(8) # 设置线程池最大线程数
        QThreadPool.globalInstance().start(worker)  # 获取全局线程池的实例并启动线程

    def _run_prediction(self):
        selected_isoforms = [
            isoform for isoform, cbox in self.cboxes.items() if cbox.isChecked()
        ]
        if not selected_isoforms:
            self.show_warning_msgbox_signal.emit(
                'No Model Selected!', 
                'Please select at least one model to start prediction.', 
                'Select Error', self.single_input_lineEdit
            )
            return
        else:
            smiles = self.single_input_lineEdit.text().strip()
            if not smiles:
                # 输入为空
                self.show_warning_msgbox_signal.emit(
                    'Please input a valid SMILES string!', None, 
                    'Input Error', self.single_input_lineEdit
                )
                return
            else:
                # 输入不合法，无法生成 mol 对象
                mol = MolFromSmiles(smiles)
                if mol is None:
                    self.show_warning_msgbox_signal.emit(
                        'Please input a valid SMILES string!', None, 
                        'Input Error', self.single_input_lineEdit
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

    def predict_1a2_inhib(self, smiles, cano_smiles, mol=None):
        pass
    
    # predict method for each isoform
    def predict_2b6_inhib(self, smiles, cano_smiles, mol=None):
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

        self.update_results(
            smiles, self.isoforms[2], final_inhib_proba_2b6, ad_2b6
        )

    def predict_2c8_inhib(self, smiles, cano_smiles, _mol=None):
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

        self.update_results(
            smiles, self.isoforms[3], final_inhib_proba_2c8, ad_2c8
        )

    def predict_2c9_inhib(self, smiles, cano_smiles, mol=None):
        pass

    def predict_2c19_inhib(self, smiles, cano_smiles, mol=None):
        pass

    def predict_2d6_inhib(self, smiles, cano_smiles, mol=None):
        pass

    def predict_3a4_inhib(self, smiles, cano_smiles, mol=None):
        pass

    def update_results(self, smiles, model, proba, ad_status):
        row = self.result_model.rowCount()

        smiles_item = QStandardItem(smiles)
        smiles_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 0, smiles_item)
        
        model_item = QStandardItem(model)
        model_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 1, model_item)

        proba_item = QStandardItem(proba)
        proba_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 2, proba_item)

        ad_item = QStandardItem(ad_status)
        ad_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_model.setItem(row, 3, ad_item)
    
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
                   for i in range(self.result_model.columnCount())]
        
        # Extract data
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
        
        # Convert to DataFrame
        df = pd.DataFrame(data, columns=['Index'] + headers)
        
        # Save to CSV
        df.to_csv(file_path, index=False)

    @Slot()
    def clear_results(self):
        self.result_model.removeRows(0, self.result_model.rowCount())

    @Slot(str, str, str, QWidget)
    def show_warning_msgbox(self, text, informative_text, title, input_widget):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText(text)
        msg_box.setInformativeText(informative_text)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setFont(QFont('Segoe UI', 11))
    
        # 显示 QMessageBox 并等待用户点击按钮，会返回一个整数值，该值对应于用户点击的按钮
        # 这个值可以用于进一步决定程序应如何响应
        return_value = msg_box.exec()
    
        if return_value == QMessageBox.StandardButton.Ok:
            # 用户点击确定后，将焦点重新定位到输入框
            input_widget.setFocus()
            # return 用于在显示警告并处理用户的响应后结束此方法或函数的执行
            return
