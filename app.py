"""
@Time : 2023/08/17 21:27
@Author : xli_0b101010
@File : app.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import sys

from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from widgets.main_window import MainWindow

# 初始化 QSplashScreen 的透明度和变化步长
splash_opacity = 0
step = 0.01
# 全局范围内声明 window，防止被垃圾回收
window = None


# QSplashScreen 默认可以通过鼠标点击来关闭窗口，重写以忽略所有的鼠标点击事件
class NonInteractiveSplashScreen(QSplashScreen):
    def mousePressEvent(self, event):
        pass


def update_opacity():
    global splash_opacity
    splash_opacity += step
    splash.setWindowOpacity(splash_opacity)
    if splash_opacity >= 1:
        timer.stop()


def load_main_window():
    global window
    # 导入 qss 样式
    with open('static/style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)

    # 创建并显示主窗口
    window = MainWindow()
    window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 保持原始的纵横比，设置想要缩放的宽度，实际的高度会自动计算
    pixmap = QPixmap('static/ecust_text_logo.png').scaled(
        QSize(750, 750), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
    )
    splash = NonInteractiveSplashScreen(pixmap)
    splash.setWindowOpacity(splash_opacity)
    splash.show()

    timer = QTimer()
    timer.timeout.connect(update_opacity)
    timer.start(15)  # 每 20ms 更新一次透明度

    # 设置一次性计时器，延迟执行指定的函数或方法
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, load_main_window)

    sys.exit(app.exec())
