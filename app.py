"""
@Time : 2023/08/17 21:27
@Author : xli_0b101010
@File : app.py
=============================================================
Just waiting for good things to happen won't change anything,
Cause I'm the one who can make changes, who make differences.
"""
import sys

from PySide6.QtWidgets import QApplication

from widgets.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 导入 qss 样式
    with open('static/style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
