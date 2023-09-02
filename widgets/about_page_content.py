"""
@Time : 2023/09/01 00:55
@Author : xli_0b101010
@File : about_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
from PySide6.QtCore import QUrl, Qt, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget

from widgets.Ui_about_page_content import Ui_aboutPageContent

class AboutPageContent(QWidget, Ui_aboutPageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.license_label.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.contact_label.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.report_btn.clicked.connect(self.open_report_url)
        self.update_btn.clicked.connect(self.open_update_url)

    @Slot()
    def open_report_url(self):
        QDesktopServices.openUrl(QUrl('https://github.com/dreamlessdrugs/Uni-CYPred/issues'))

    @Slot()
    def open_update_url(self):
        QDesktopServices.openUrl(QUrl('https://github.com/dreamlessdrugs/Uni-CYPred/releases'))
