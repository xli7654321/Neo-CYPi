# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import static.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 667)
        MainWindow.setMinimumSize(QSize(1000, 667))
        MainWindow.setMaximumSize(QSize(1000, 667))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMinimumSize(QSize(864, 642))
        self.content_widget.setMaximumSize(QSize(864, 642))
        self.content_widget.setFont(font)
        self.content_vLayout = QVBoxLayout(self.content_widget)
        self.content_vLayout.setSpacing(0)
        self.content_vLayout.setObjectName(u"content_vLayout")
        self.content_vLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.stackedWidget.addWidget(self.home_page)
        self.single_page = QWidget()
        self.single_page.setObjectName(u"single_page")
        self.stackedWidget.addWidget(self.single_page)
        self.batch_page = QWidget()
        self.batch_page.setObjectName(u"batch_page")
        self.stackedWidget.addWidget(self.batch_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.stackedWidget.addWidget(self.about_page)

        self.content_vLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.content_widget, 0, 1, 1, 1)

        self.statusbar_widget = QWidget(self.centralwidget)
        self.statusbar_widget.setObjectName(u"statusbar_widget")
        self.statusbar_widget.setMinimumSize(QSize(864, 25))
        self.statusbar_widget.setMaximumSize(QSize(864, 25))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.statusbar_widget.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.statusbar_widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 1, 15, 0)
        self.horizontalSpacer = QSpacerItem(690, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loading_widget = QWidget(self.statusbar_widget)
        self.loading_widget.setObjectName(u"loading_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loading_widget.sizePolicy().hasHeightForWidth())
        self.loading_widget.setSizePolicy(sizePolicy)
        self.loading_widget.setMinimumSize(QSize(20, 20))
        self.loading_widget.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.loading_widget)

        self.status_label = QLabel(self.statusbar_widget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMinimumSize(QSize(130, 24))
        self.status_label.setMaximumSize(QSize(130, 24))
        self.status_label.setScaledContents(False)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.status_label)


        self.gridLayout.addWidget(self.statusbar_widget, 1, 1, 1, 1)

        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setMinimumSize(QSize(136, 667))
        self.sidebar_widget.setMaximumSize(QSize(136, 667))
        self.sidebar_vLayout = QVBoxLayout(self.sidebar_widget)
        self.sidebar_vLayout.setSpacing(0)
        self.sidebar_vLayout.setObjectName(u"sidebar_vLayout")
        self.sidebar_vLayout.setContentsMargins(0, 6, 0, 0)
        self.logo_label = QLabel(self.sidebar_widget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(136, 60))
        self.logo_label.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.logo_label.setFont(font2)
        self.logo_label.setScaledContents(False)
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.sidebar_vLayout.addWidget(self.logo_label)

        self.sidebar_btn_vLayout = QVBoxLayout()
        self.sidebar_btn_vLayout.setSpacing(0)
        self.sidebar_btn_vLayout.setObjectName(u"sidebar_btn_vLayout")
        self.sidebar_btn_vLayout.setContentsMargins(-1, 0, -1, -1)
        self.home_btn = QPushButton(self.sidebar_widget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(135, 60))
        self.home_btn.setMaximumSize(QSize(16777215, 16777215))
        self.home_btn.setFont(font)
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)

        self.sidebar_btn_vLayout.addWidget(self.home_btn)

        self.single_btn = QPushButton(self.sidebar_widget)
        self.single_btn.setObjectName(u"single_btn")
        self.single_btn.setMinimumSize(QSize(135, 60))
        self.single_btn.setMaximumSize(QSize(16777215, 16777215))
        self.single_btn.setFont(font)
        self.single_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.single_btn.setCheckable(True)
        self.single_btn.setAutoExclusive(True)

        self.sidebar_btn_vLayout.addWidget(self.single_btn)

        self.batch_btn = QPushButton(self.sidebar_widget)
        self.batch_btn.setObjectName(u"batch_btn")
        self.batch_btn.setMinimumSize(QSize(135, 60))
        self.batch_btn.setFont(font)
        self.batch_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.batch_btn.setCheckable(True)
        self.batch_btn.setAutoExclusive(True)

        self.sidebar_btn_vLayout.addWidget(self.batch_btn)

        self.about_btn = QPushButton(self.sidebar_widget)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(135, 60))
        self.about_btn.setFont(font)
        self.about_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_btn.setCheckable(True)
        self.about_btn.setAutoExclusive(True)

        self.sidebar_btn_vLayout.addWidget(self.about_btn)


        self.sidebar_vLayout.addLayout(self.sidebar_btn_vLayout)

        self.verticalSpacer = QSpacerItem(20, 221, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sidebar_vLayout.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.sidebar_widget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(136, 60))
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.sidebar_vLayout.addWidget(self.exit_btn)


        self.gridLayout.addWidget(self.sidebar_widget, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Uni-CYPred", None))
        self.status_label.setText("")
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"Uni-CYPred", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.single_btn.setText(QCoreApplication.translate("MainWindow", u"Single Molecule\n"
"Prediction", None))
        self.batch_btn.setText(QCoreApplication.translate("MainWindow", u"Batch\n"
"Prediction", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

