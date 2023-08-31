# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'single_page_content.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import static.resource_rc

class Ui_singlePageContent(object):
    def setupUi(self, singlePageContent):
        if not singlePageContent.objectName():
            singlePageContent.setObjectName(u"singlePageContent")
        singlePageContent.resize(864, 642)
        singlePageContent.setMinimumSize(QSize(864, 642))
        singlePageContent.setMaximumSize(QSize(864, 642))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        singlePageContent.setFont(font)
        singlePageContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.single_scrollArea = QScrollArea(singlePageContent)
        self.single_scrollArea.setObjectName(u"single_scrollArea")
        self.single_scrollArea.setGeometry(QRect(0, 0, 864, 642))
        self.single_scrollArea.setFrameShape(QFrame.NoFrame)
        self.single_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.single_scrollArea.setWidgetResizable(True)
        self.single_scrollAreaWidgetContents = QWidget()
        self.single_scrollAreaWidgetContents.setObjectName(u"single_scrollAreaWidgetContents")
        self.single_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 623))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.single_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.single_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.single_scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.single_scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 0, 40, 0)
        self.verticalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.single_headline_hlay = QHBoxLayout()
        self.single_headline_hlay.setSpacing(6)
        self.single_headline_hlay.setObjectName(u"single_headline_hlay")
        self.single_icon = QLabel(self.single_scrollAreaWidgetContents)
        self.single_icon.setObjectName(u"single_icon")
        sizePolicy.setHeightForWidth(self.single_icon.sizePolicy().hasHeightForWidth())
        self.single_icon.setSizePolicy(sizePolicy)
        self.single_icon.setMaximumSize(QSize(20, 20))
        self.single_icon.setPixmap(QPixmap(u":/icons/icons/Microsoft-Fluentui-Emoji-Mono-Dna.ico"))
        self.single_icon.setScaledContents(True)
        self.single_icon.setAlignment(Qt.AlignCenter)

        self.single_headline_hlay.addWidget(self.single_icon)

        self.single_label = QLabel(self.single_scrollAreaWidgetContents)
        self.single_label.setObjectName(u"single_label")
        sizePolicy.setHeightForWidth(self.single_label.sizePolicy().hasHeightForWidth())
        self.single_label.setSizePolicy(sizePolicy)
        self.single_label.setMinimumSize(QSize(0, 26))
        self.single_label.setMaximumSize(QSize(16777215, 26))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.single_label.setFont(font1)
        self.single_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.single_headline_hlay.addWidget(self.single_label)


        self.verticalLayout.addLayout(self.single_headline_hlay)

        self.verticalSpacer_4 = QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.single_gridLayout = QGridLayout()
        self.single_gridLayout.setObjectName(u"single_gridLayout")
        self.single_gridLayout.setHorizontalSpacing(12)
        self.single_gridLayout.setVerticalSpacing(0)
        self.single_gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.single_input_lineEdit = QLineEdit(self.single_scrollAreaWidgetContents)
        self.single_input_lineEdit.setObjectName(u"single_input_lineEdit")
        self.single_input_lineEdit.setFont(font)

        self.single_gridLayout.addWidget(self.single_input_lineEdit, 1, 0, 1, 1)

        self.single_input_label = QLabel(self.single_scrollAreaWidgetContents)
        self.single_input_label.setObjectName(u"single_input_label")
        sizePolicy.setHeightForWidth(self.single_input_label.sizePolicy().hasHeightForWidth())
        self.single_input_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.single_input_label.setFont(font2)

        self.single_gridLayout.addWidget(self.single_input_label, 0, 0, 1, 1)

        self.single_example_btn = QPushButton(self.single_scrollAreaWidgetContents)
        self.single_example_btn.setObjectName(u"single_example_btn")
        self.single_example_btn.setMinimumSize(QSize(80, 0))
        self.single_example_btn.setFont(font)
        self.single_example_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.single_gridLayout.addWidget(self.single_example_btn, 1, 1, 1, 1)

        self.single_gridLayout.setRowMinimumHeight(0, 40)

        self.verticalLayout.addLayout(self.single_gridLayout)

        self.verticalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(125, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.single_start_btn = QPushButton(self.single_scrollAreaWidgetContents)
        self.single_start_btn.setObjectName(u"single_start_btn")
        self.single_start_btn.setMinimumSize(QSize(0, 30))
        self.single_start_btn.setMaximumSize(QSize(16777215, 30))
        self.single_start_btn.setFont(font)
        self.single_start_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.single_start_btn)

        self.horizontalSpacer = QSpacerItem(125, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.single_result_groupbox = QGroupBox(self.single_scrollAreaWidgetContents)
        self.single_result_groupbox.setObjectName(u"single_result_groupbox")
        self.single_result_groupbox.setMinimumSize(QSize(0, 360))
        self.single_result_groupbox.setFont(font1)
        self.single_result_groupbox.setAlignment(Qt.AlignCenter)
        self.single_result_groupbox.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.single_result_groupbox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.single_table = QTableView(self.single_result_groupbox)
        self.single_table.setObjectName(u"single_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.single_table.sizePolicy().hasHeightForWidth())
        self.single_table.setSizePolicy(sizePolicy1)
        self.single_table.setMinimumSize(QSize(0, 290))
        self.single_table.setFont(font)

        self.verticalLayout_2.addWidget(self.single_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.single_save_btn = QPushButton(self.single_result_groupbox)
        self.single_save_btn.setObjectName(u"single_save_btn")
        self.single_save_btn.setFont(font)
        self.single_save_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.single_save_btn)

        self.single_clear_btn = QPushButton(self.single_result_groupbox)
        self.single_clear_btn.setObjectName(u"single_clear_btn")
        self.single_clear_btn.setFont(font)
        self.single_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.single_clear_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.single_result_groupbox)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.single_scrollArea.setWidget(self.single_scrollAreaWidgetContents)

        self.retranslateUi(singlePageContent)

        QMetaObject.connectSlotsByName(singlePageContent)
    # setupUi

    def retranslateUi(self, singlePageContent):
        singlePageContent.setWindowTitle(QCoreApplication.translate("singlePageContent", u"singlePageContent", None))
        self.single_icon.setText("")
        self.single_label.setText(QCoreApplication.translate("singlePageContent", u"Single-Molecule Prediction", None))
        self.single_input_lineEdit.setPlaceholderText(QCoreApplication.translate("singlePageContent", u"CC(C)(C)NCc1cc(Nc2ccnc3cc(Cl)ccc23)ccc1F", None))
        self.single_input_label.setText(QCoreApplication.translate("singlePageContent", u"<html><head/><body><p>Please input a <span style=\" font-weight:700; color:#0055ff;\">SMILES</span> string for prediction:</p></body></html>", None))
        self.single_example_btn.setText(QCoreApplication.translate("singlePageContent", u"Example", None))
        self.single_start_btn.setText(QCoreApplication.translate("singlePageContent", u"START PREDICTION", None))
        self.single_result_groupbox.setTitle(QCoreApplication.translate("singlePageContent", u"Results", None))
        self.single_save_btn.setText(QCoreApplication.translate("singlePageContent", u"Save Results", None))
        self.single_clear_btn.setText(QCoreApplication.translate("singlePageContent", u"Clear Results", None))
    # retranslateUi

