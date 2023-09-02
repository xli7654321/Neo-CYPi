# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batch_page_content.ui'
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

class Ui_batchPageContent(object):
    def setupUi(self, batchPageContent):
        if not batchPageContent.objectName():
            batchPageContent.setObjectName(u"batchPageContent")
        batchPageContent.resize(864, 642)
        batchPageContent.setMinimumSize(QSize(864, 642))
        batchPageContent.setMaximumSize(QSize(864, 642))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        batchPageContent.setFont(font)
        batchPageContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.batch_scrollArea = QScrollArea(batchPageContent)
        self.batch_scrollArea.setObjectName(u"batch_scrollArea")
        self.batch_scrollArea.setGeometry(QRect(0, 0, 864, 642))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_scrollArea.sizePolicy().hasHeightForWidth())
        self.batch_scrollArea.setSizePolicy(sizePolicy)
        self.batch_scrollArea.setFrameShape(QFrame.NoFrame)
        self.batch_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.batch_scrollArea.setWidgetResizable(True)
        self.batch_scrollAreaWidgetContents = QWidget()
        self.batch_scrollAreaWidgetContents.setObjectName(u"batch_scrollAreaWidgetContents")
        self.batch_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 623))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.batch_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.batch_scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.batch_scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.batch_scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 0, 40, 0)
        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.batch_headline_hlay = QHBoxLayout()
        self.batch_headline_hlay.setSpacing(6)
        self.batch_headline_hlay.setObjectName(u"batch_headline_hlay")
        self.batch_icon = QLabel(self.batch_scrollAreaWidgetContents)
        self.batch_icon.setObjectName(u"batch_icon")
        self.batch_icon.setMaximumSize(QSize(20, 20))
        self.batch_icon.setPixmap(QPixmap(u":/icons/icons/Microsoft-Fluentui-Emoji-Mono-Infinity.ico"))
        self.batch_icon.setScaledContents(True)
        self.batch_icon.setAlignment(Qt.AlignCenter)

        self.batch_headline_hlay.addWidget(self.batch_icon)

        self.batch_label = QLabel(self.batch_scrollAreaWidgetContents)
        self.batch_label.setObjectName(u"batch_label")
        sizePolicy1.setHeightForWidth(self.batch_label.sizePolicy().hasHeightForWidth())
        self.batch_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.batch_label.setFont(font1)
        self.batch_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.batch_headline_hlay.addWidget(self.batch_label)


        self.verticalLayout.addLayout(self.batch_headline_hlay)

        self.verticalSpacer_4 = QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.batch_gridLayout = QGridLayout()
        self.batch_gridLayout.setObjectName(u"batch_gridLayout")
        self.batch_gridLayout.setHorizontalSpacing(12)
        self.batch_gridLayout.setVerticalSpacing(0)
        self.batch_gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.batch_input_lineEdit = QLineEdit(self.batch_scrollAreaWidgetContents)
        self.batch_input_lineEdit.setObjectName(u"batch_input_lineEdit")
        self.batch_input_lineEdit.setFont(font)
        self.batch_input_lineEdit.setReadOnly(True)

        self.batch_gridLayout.addWidget(self.batch_input_lineEdit, 1, 0, 1, 1)

        self.batch_input_label = QLabel(self.batch_scrollAreaWidgetContents)
        self.batch_input_label.setObjectName(u"batch_input_label")
        sizePolicy1.setHeightForWidth(self.batch_input_label.sizePolicy().hasHeightForWidth())
        self.batch_input_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(13)
        self.batch_input_label.setFont(font2)
        self.batch_input_label.setCursor(QCursor(Qt.IBeamCursor))
        self.batch_input_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.batch_gridLayout.addWidget(self.batch_input_label, 0, 0, 1, 1)

        self.batch_browse_btn = QPushButton(self.batch_scrollAreaWidgetContents)
        self.batch_browse_btn.setObjectName(u"batch_browse_btn")
        self.batch_browse_btn.setMinimumSize(QSize(80, 0))
        self.batch_browse_btn.setFont(font)
        self.batch_browse_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.batch_gridLayout.addWidget(self.batch_browse_btn, 1, 1, 1, 1)

        self.batch_gridLayout.setRowMinimumHeight(0, 40)

        self.verticalLayout.addLayout(self.batch_gridLayout)

        self.verticalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(125, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.batch_start_btn = QPushButton(self.batch_scrollAreaWidgetContents)
        self.batch_start_btn.setObjectName(u"batch_start_btn")
        self.batch_start_btn.setFont(font)
        self.batch_start_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.batch_start_btn)

        self.horizontalSpacer = QSpacerItem(125, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.batch_result_groupbox = QGroupBox(self.batch_scrollAreaWidgetContents)
        self.batch_result_groupbox.setObjectName(u"batch_result_groupbox")
        self.batch_result_groupbox.setMinimumSize(QSize(0, 360))
        self.batch_result_groupbox.setFont(font1)
        self.batch_result_groupbox.setAlignment(Qt.AlignCenter)
        self.batch_result_groupbox.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.batch_result_groupbox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.batch_table = QTableView(self.batch_result_groupbox)
        self.batch_table.setObjectName(u"batch_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.batch_table.sizePolicy().hasHeightForWidth())
        self.batch_table.setSizePolicy(sizePolicy2)
        self.batch_table.setMinimumSize(QSize(0, 290))
        self.batch_table.setFont(font)

        self.verticalLayout_2.addWidget(self.batch_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.batch_save_btn = QPushButton(self.batch_result_groupbox)
        self.batch_save_btn.setObjectName(u"batch_save_btn")
        self.batch_save_btn.setFont(font)
        self.batch_save_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.batch_save_btn)

        self.batch_clear_btn = QPushButton(self.batch_result_groupbox)
        self.batch_clear_btn.setObjectName(u"batch_clear_btn")
        self.batch_clear_btn.setFont(font)
        self.batch_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.batch_clear_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.batch_result_groupbox)

        self.verticalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.batch_scrollArea.setWidget(self.batch_scrollAreaWidgetContents)

        self.retranslateUi(batchPageContent)

        QMetaObject.connectSlotsByName(batchPageContent)
    # setupUi

    def retranslateUi(self, batchPageContent):
        batchPageContent.setWindowTitle(QCoreApplication.translate("batchPageContent", u"batchPageContent", None))
        self.batch_icon.setText("")
        self.batch_label.setText(QCoreApplication.translate("batchPageContent", u"Batch-Molecule Prediction", None))
        self.batch_input_lineEdit.setPlaceholderText(QCoreApplication.translate("batchPageContent", u"No file chosen", None))
        self.batch_input_label.setText(QCoreApplication.translate("batchPageContent", u"<html><head/><body><p>Please upload a <span style=\" font-weight:700; color:#0055ff;\">txt</span> or <span style=\" font-weight:700; color:#0055ff;\">sdf</span> format file for prediction:</p></body></html>", None))
        self.batch_browse_btn.setText(QCoreApplication.translate("batchPageContent", u"Browse", None))
        self.batch_start_btn.setText(QCoreApplication.translate("batchPageContent", u"START PREDICTION", None))
        self.batch_result_groupbox.setTitle(QCoreApplication.translate("batchPageContent", u"Results", None))
#if QT_CONFIG(tooltip)
        self.batch_save_btn.setToolTip(QCoreApplication.translate("batchPageContent", u"Save Results as CSV Format File", None))
#endif // QT_CONFIG(tooltip)
        self.batch_save_btn.setText(QCoreApplication.translate("batchPageContent", u"Save Results", None))
        self.batch_clear_btn.setText(QCoreApplication.translate("batchPageContent", u"Clear Results", None))
    # retranslateUi

