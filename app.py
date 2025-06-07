import sys
from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen
from widgets.main_window import MainWindow

# QSplashScreen can be closed by clicking on it,
# override to ignore all mouse click events
class NonInteractiveSplashScreen(QSplashScreen):
    def mousePressEvent(self, event):
        pass

class SplashAnimator:
    def __init__(self, splash):
        self.splash = splash
        self.opacity = 0.0
        self.step = 0.01
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_opacity)
        self.timer.start(15)
        
    def update_opacity(self):
        self.opacity += self.step
        self.splash.setWindowOpacity(self.opacity)
        if self.opacity >= 1:
            self.timer.stop()
    
    def stop(self):
        # a 2-second delay
        QTimer.singleShot(2000, self.splash.close)

class MainWindowLoader:
    def __init__(self):
        # Declare window in the global scope to prevent it from being garbage collected
        self.window = None
    
    def load(self):
        self.window = MainWindow()
        self.window.show()
    
    def run(self):
        # a 2-second delay
        QTimer.singleShot(2000, self.load)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('static/style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)

    pixmap = QPixmap('static/splash.png').scaled(
        QSize(750, 750),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation
    )
    splash = NonInteractiveSplashScreen(pixmap)
    splash.setWindowOpacity(0)
    splash.show()
    animator = SplashAnimator(splash)
    animator.stop()

    loader = MainWindowLoader()
    loader.run()

    sys.exit(app.exec())
