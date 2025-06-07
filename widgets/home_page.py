from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui.Ui_home_page import Ui_homePage

class HomePage(QWidget, Ui_homePage):
    jump_to_single = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pred_btn.clicked.connect(self.jump_to_single.emit)
