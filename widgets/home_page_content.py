"""
@Time : 2023/09/01 00:37
@Author : xli_0b101010
@File : home_page_content.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
from PySide6.QtCore import QUrl, Qt, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget

from widgets.Ui_home_page_content import Ui_homePageContent

class HomePageContent(QWidget, Ui_homePageContent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.doc_label.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.github_btn.clicked.connect(self.open_github_url)

    @Slot()
    def open_github_url(self):
        QDesktopServices.openUrl(QUrl('https://github.com/dreamlessdrugs/Uni-CYPred'))
