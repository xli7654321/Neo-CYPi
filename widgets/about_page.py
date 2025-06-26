from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget
from ui.Ui_about_page import Ui_aboutPage

class AboutPage(QWidget, Ui_aboutPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.report_btn.clicked.connect(self.open_report_url)
        self.update_btn.clicked.connect(self.open_update_url)

    @Slot()
    def open_report_url(self):
        QDesktopServices.openUrl(QUrl('https://github.com/xli7654321/NEXT-CYPInh/issues'))

    @Slot()
    def open_update_url(self):
        QDesktopServices.openUrl(QUrl('https://github.com/xli7654321/NEXT-CYPInh/releases'))
