"""
@Time : 2023/08/18 01:54
@Author : xli_0b101010
@File : main_window.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from widgets.Ui_main import Ui_MainWindow
from widgets.batch_page_content import BatchPageContent
from widgets.single_page_content import SinglePageContent
from widgets.spinner import WaitingSpinner


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # 初始化主页面 - 多继承
        self.setupUi(self)

        # 初始化各个页面的内容
        self.single_page_content = SinglePageContent()
        self.batch_page_content = BatchPageContent()

        self.add_home_page_content()
        self.add_single_page_content()
        self.add_batch_page_content()
        self.add_about_page_content()

        # 设置默认显示的页面
        self.stackedWidget.setCurrentIndex(0)
        self.home_btn.setChecked(True)

        # 绑定 sidebar 按钮的 toggled 信号到槽函数
        self.home_btn.toggled.connect(self.on_home_btn_toggled)
        self.single_btn.toggled.connect(self.on_single_btn_toggled)
        self.batch_btn.toggled.connect(self.on_batch_btn_toggled)
        self.about_btn.toggled.connect(self.on_about_btn_toggled)

        # statusbar loading spinner
        self.loading_spinner = WaitingSpinner(
            self.loading_widget,
            roundness=100.00,
            opacity=0.00,
            fade=75.00,
            lines=7,
            line_length=7,
            line_width=2,
            radius=3,
            speed=1.25,
            color=QColor(0, 85, 255)
        )

        self.running_prediction_counts = 0

        self.single_page_content.start_loading.connect(self.start_loading)
        self.single_page_content.finish_loading.connect(self.finish_loading)
        self.batch_page_content.start_loading.connect(self.start_loading)
        self.batch_page_content.finish_loading.connect(self.finish_loading)

    def add_home_page_content(self):
        pass

    def add_single_page_content(self):
        # layout 充当一个添加 single_page 的角色
        layout = QVBoxLayout(self.single_page)  # single_page 来源于 ui
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.single_page_content)

    def add_batch_page_content(self):
        layout = QVBoxLayout(self.batch_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.batch_page_content)

    def add_about_page_content(self):
        pass

    # 切换界面的槽函数
    @Slot(bool)
    def on_home_btn_toggled(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(0)

    @Slot(bool)
    def on_single_btn_toggled(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(1)

    @Slot(bool)
    def on_batch_btn_toggled(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(2)

    @Slot(bool)
    def on_about_btn_toggled(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(3)

    @Slot()
    def start_loading(self):
        self.running_prediction_counts += 1
        self.loading_spinner.start()
        self.status_label.setText('Running Prediction....')

    @Slot()
    def finish_loading(self):
        self.running_prediction_counts -= 1
        if self.running_prediction_counts == 0:
            self.loading_spinner.stop()
            self.status_label.setText('Waiting for Prediction')
