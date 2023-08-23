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
        singlePageContent.resize(714, 610)
        singlePageContent.setMinimumSize(QSize(714, 610))
        singlePageContent.setMaximumSize(QSize(714, 610))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        singlePageContent.setFont(font)
        singlePageContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.single_scrollArea = QScrollArea(singlePageContent)
        self.single_scrollArea.setObjectName(u"single_scrollArea")
        self.single_scrollArea.setGeometry(QRect(0, 0, 714, 610))
        self.single_scrollArea.setFrameShape(QFrame.NoFrame)
        self.single_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.single_scrollArea.setWidgetResizable(True)
        self.single_scrollAreaWidgetContents = QWidget()
        self.single_scrollAreaWidgetContents.setObjectName(u"single_scrollAreaWidgetContents")
        self.single_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 610))
        self.single_scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.single_scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 20, 40, 0)
        self.single_headline_hlay = QHBoxLayout()
        self.single_headline_hlay.setSpacing(6)
        self.single_headline_hlay.setObjectName(u"single_headline_hlay")
        self.single_icon = QLabel(self.single_scrollAreaWidgetContents)
        self.single_icon.setObjectName(u"single_icon")
        self.single_icon.setMaximumSize(QSize(20, 20))
        self.single_icon.setPixmap(QPixmap(u":/icons/icons/Microsoft-Fluentui-Emoji-Mono-Dna.ico"))
        self.single_icon.setScaledContents(True)
        self.single_icon.setAlignment(Qt.AlignCenter)

        self.single_headline_hlay.addWidget(self.single_icon)

        self.single_label = QLabel(self.single_scrollAreaWidgetContents)
        self.single_label.setObjectName(u"single_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.single_label.setFont(font1)
        self.single_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.single_headline_hlay.addWidget(self.single_label)


        self.verticalLayout.addLayout(self.single_headline_hlay)

        self.verticalSpacer_4 = QSpacerItem(0, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.single_gridLayout = QGridLayout()
        self.single_gridLayout.setObjectName(u"single_gridLayout")
        self.single_gridLayout.setHorizontalSpacing(10)
        self.single_gridLayout.setVerticalSpacing(0)
        self.single_gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.single_input_lineEdit = QLineEdit(self.single_scrollAreaWidgetContents)
        self.single_input_lineEdit.setObjectName(u"single_input_lineEdit")
        self.single_input_lineEdit.setFont(font)

        self.single_gridLayout.addWidget(self.single_input_lineEdit, 1, 0, 1, 1)

        self.single_input_label = QLabel(self.single_scrollAreaWidgetContents)
        self.single_input_label.setObjectName(u"single_input_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.single_input_label.setFont(font2)

        self.single_gridLayout.addWidget(self.single_input_label, 0, 0, 1, 1)

        self.single_example_btn = QPushButton(self.single_scrollAreaWidgetContents)
        self.single_example_btn.setObjectName(u"single_example_btn")
        self.single_example_btn.setMinimumSize(QSize(80, 0))
        self.single_example_btn.setFont(font)

        self.single_gridLayout.addWidget(self.single_example_btn, 1, 1, 1, 1)

        self.single_gridLayout.setRowMinimumHeight(0, 40)

        self.verticalLayout.addLayout(self.single_gridLayout)

        self.verticalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.single_start_btn = QPushButton(self.single_scrollAreaWidgetContents)
        self.single_start_btn.setObjectName(u"single_start_btn")
        self.single_start_btn.setFont(font)

        self.horizontalLayout_2.addWidget(self.single_start_btn)

        self.horizontalSpacer = QSpacerItem(300, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(0, 45, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.single_result_groupbox = QGroupBox(self.single_scrollAreaWidgetContents)
        self.single_result_groupbox.setObjectName(u"single_result_groupbox")
        self.single_result_groupbox.setFont(font1)
        self.single_result_groupbox.setAlignment(Qt.AlignCenter)
        self.single_result_groupbox.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.single_result_groupbox)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 75)
        self.single_tableview = QTableView(self.single_result_groupbox)
        self.single_tableview.setObjectName(u"single_tableview")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.single_tableview.sizePolicy().hasHeightForWidth())
        self.single_tableview.setSizePolicy(sizePolicy)
        self.single_tableview.setMinimumSize(QSize(0, 227))
        self.single_tableview.setFont(font)

        self.horizontalLayout.addWidget(self.single_tableview)

        self.single_download_vlay = QVBoxLayout()
        self.single_download_vlay.setSpacing(0)
        self.single_download_vlay.setObjectName(u"single_download_vlay")
        self.single_download_btn = QPushButton(self.single_result_groupbox)
        self.single_download_btn.setObjectName(u"single_download_btn")
        self.single_download_btn.setMinimumSize(QSize(95, 0))
        self.single_download_btn.setFont(font)

        self.single_download_vlay.addWidget(self.single_download_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.single_download_vlay.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.single_download_vlay)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addWidget(self.single_result_groupbox)

        self.single_scrollArea.setWidget(self.single_scrollAreaWidgetContents)

        self.retranslateUi(singlePageContent)

        QMetaObject.connectSlotsByName(singlePageContent)
    # setupUi

    def retranslateUi(self, singlePageContent):
        singlePageContent.setWindowTitle(QCoreApplication.translate("singlePageContent", u"singlePageContent", None))
        self.single_icon.setText("")
        self.single_label.setText(QCoreApplication.translate("singlePageContent", u"Single-Molecule Prediction", None))
        self.single_input_lineEdit.setPlaceholderText(QCoreApplication.translate("singlePageContent", u"CC(C)(C)NCc1cc(Nc2ccnc3cc(Cl)ccc23)ccc1F", None))
        self.single_input_label.setText(QCoreApplication.translate("singlePageContent", u"Please input a SMILES string for prediction:", None))
        self.single_example_btn.setText(QCoreApplication.translate("singlePageContent", u"Example", None))
        self.single_start_btn.setText(QCoreApplication.translate("singlePageContent", u"START PREDICTION", None))
        self.single_result_groupbox.setTitle(QCoreApplication.translate("singlePageContent", u"Results", None))
#if QT_CONFIG(tooltip)
        self.single_download_btn.setToolTip(QCoreApplication.translate("singlePageContent", u"Download results as CSV format file", None))
#endif // QT_CONFIG(tooltip)
        self.single_download_btn.setText(QCoreApplication.translate("singlePageContent", u"Download\n"
"Results", None))
    # retranslateUi

