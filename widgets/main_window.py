"""
@Time : 2023/08/18 01:54
@Author : xli_0b101010
@File : main_window.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from widgets.Ui_main import Ui_MainWindow
from widgets.batch_page_content import batchPageContent
from widgets.single_page_content import singlePageContent


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # 初始化主页面 - 多继承
        self.setupUi(self)

        # 初始化各个页面的内容
        self.single_page_content = singlePageContent()
        self.batch_page_content = batchPageContent()

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

        self.statusbar_active = False
        self.statusbar_widget.mousePressEvent = self.toggle_statusbar_style

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

    def toggle_statusbar_style(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.statusbar_active = not self.statusbar_active
            if self.statusbar_active:
                self.statusbar_widget.setStyleSheet('border-top: 1px solid coral;')
            else:
                self.statusbar_widget.setStyleSheet('border-top: 1px solid lightslategray;')
        # 重写 mousePressEvent 后确保原有的事件不会被覆盖
        super().mousePressEvent(event)
