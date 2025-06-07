from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout
from ui.Ui_main import Ui_MainWindow
from widgets.about_page import AboutPage
from widgets.batch_page import BatchPage
from widgets.home_page import HomePage
from widgets.single_page import SinglePage
from widgets.spinner import WaitingSpinner

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Initialize main window - multiple inheritance
        self.setupUi(self)

        # Initialize pages
        self.home_page_widget = HomePage()
        self.single_page_widget = SinglePage()
        self.batch_page_widget = BatchPage()
        self.about_page_widget = AboutPage()

        self.add_home_page()
        self.add_single_page()
        self.add_batch_page()
        self.add_about_page()

        # Set the default displayed page
        self.stackedWidget.setCurrentIndex(0)
        self.home_btn.setChecked(True)

        # Bind the toggled signal of sidebar buttons to slot functions
        self.home_btn.toggled.connect(self.on_home_btn_toggled)
        self.single_btn.toggled.connect(self.on_single_btn_toggled)
        self.batch_btn.toggled.connect(self.on_batch_btn_toggled)
        self.about_btn.toggled.connect(self.on_about_btn_toggled)
        
        self.home_page_widget.jump_to_single.connect(self.show_single_page)

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

        self.single_page_widget.start_loading.connect(self.start_loading)
        self.single_page_widget.finish_loading.connect(self.finish_loading)
        self.batch_page_widget.start_loading.connect(self.start_loading)
        self.batch_page_widget.finish_loading.connect(self.finish_loading)

        self.exit_btn.clicked.connect(self.close)

    def add_home_page(self):
        # layout acts as a container to add the home_page
        layout = QVBoxLayout(self.home_page)  # home_page comes from ui
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.home_page_widget)

    def add_single_page(self):
        layout = QVBoxLayout(self.single_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.single_page_widget)

    def add_batch_page(self):
        layout = QVBoxLayout(self.batch_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.batch_page_widget)

    def add_about_page(self):
        layout = QVBoxLayout(self.about_page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.about_page_widget)

    # Slot functions to switch pages
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
    def show_single_page(self):
        self.single_btn.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)

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
            self.status_label.setText('')
    
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 
            'Confirm Exit', 
            'Are you sure you want to exit?', 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
