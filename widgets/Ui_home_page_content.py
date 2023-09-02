# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page_content.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import static.resource_rc

class Ui_homePageContent(object):
    def setupUi(self, homePageContent):
        if not homePageContent.objectName():
            homePageContent.setObjectName(u"homePageContent")
        homePageContent.resize(864, 642)
        homePageContent.setMinimumSize(QSize(864, 642))
        homePageContent.setMaximumSize(QSize(864, 642))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        homePageContent.setFont(font)
        homePageContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.home_scrollArea = QScrollArea(homePageContent)
        self.home_scrollArea.setObjectName(u"home_scrollArea")
        self.home_scrollArea.setGeometry(QRect(0, 0, 864, 642))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_scrollArea.sizePolicy().hasHeightForWidth())
        self.home_scrollArea.setSizePolicy(sizePolicy)
        self.home_scrollArea.setFrameShape(QFrame.NoFrame)
        self.home_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.home_scrollArea.setWidgetResizable(True)
        self.home_scrollAreaWidgetContents = QWidget()
        self.home_scrollAreaWidgetContents.setObjectName(u"home_scrollAreaWidgetContents")
        self.home_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 654))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.home_scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.home_scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 0, 40, 0)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.home_headline_hlay = QHBoxLayout()
        self.home_headline_hlay.setSpacing(6)
        self.home_headline_hlay.setObjectName(u"home_headline_hlay")
        self.home_icon = QLabel(self.home_scrollAreaWidgetContents)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setMaximumSize(QSize(20, 20))
        self.home_icon.setPixmap(QPixmap(u":/icons/icons/Ionic-Ionicons-Home.ico"))
        self.home_icon.setScaledContents(True)
        self.home_icon.setAlignment(Qt.AlignCenter)

        self.home_headline_hlay.addWidget(self.home_icon)

        self.home_label = QLabel(self.home_scrollAreaWidgetContents)
        self.home_label.setObjectName(u"home_label")
        sizePolicy1.setHeightForWidth(self.home_label.sizePolicy().hasHeightForWidth())
        self.home_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.home_label.setFont(font1)
        self.home_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.home_headline_hlay.addWidget(self.home_label)


        self.verticalLayout.addLayout(self.home_headline_hlay)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.home_title_label = QLabel(self.home_scrollAreaWidgetContents)
        self.home_title_label.setObjectName(u"home_title_label")
        sizePolicy1.setHeightForWidth(self.home_title_label.sizePolicy().hasHeightForWidth())
        self.home_title_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.home_title_label.setFont(font2)
        self.home_title_label.setFrameShape(QFrame.NoFrame)
        self.home_title_label.setFrameShadow(QFrame.Plain)
        self.home_title_label.setTextFormat(Qt.PlainText)
        self.home_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.home_title_label)

        self.version_label = QLabel(self.home_scrollAreaWidgetContents)
        self.version_label.setObjectName(u"version_label")
        sizePolicy1.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy1)
        self.version_label.setFont(font)
        self.version_label.setCursor(QCursor(Qt.IBeamCursor))
        self.version_label.setMouseTracking(True)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.version_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.version_label)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.home_headline_hlay_2 = QHBoxLayout()
        self.home_headline_hlay_2.setSpacing(6)
        self.home_headline_hlay_2.setObjectName(u"home_headline_hlay_2")
        self.home_icon_2 = QLabel(self.home_scrollAreaWidgetContents)
        self.home_icon_2.setObjectName(u"home_icon_2")
        self.home_icon_2.setMaximumSize(QSize(20, 20))
        self.home_icon_2.setPixmap(QPixmap(u":/icons/icons/Microsoft-Fluentui-Emoji-Mono-Magic-Wand.ico"))
        self.home_icon_2.setScaledContents(True)
        self.home_icon_2.setAlignment(Qt.AlignCenter)

        self.home_headline_hlay_2.addWidget(self.home_icon_2)

        self.start_label = QLabel(self.home_scrollAreaWidgetContents)
        self.start_label.setObjectName(u"start_label")
        sizePolicy1.setHeightForWidth(self.start_label.sizePolicy().hasHeightForWidth())
        self.start_label.setSizePolicy(sizePolicy1)
        self.start_label.setFont(font1)
        self.start_label.setCursor(QCursor(Qt.IBeamCursor))
        self.start_label.setTextFormat(Qt.RichText)
        self.start_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.home_headline_hlay_2.addWidget(self.start_label)


        self.verticalLayout.addLayout(self.home_headline_hlay_2)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.start_single_title_label = QLabel(self.home_scrollAreaWidgetContents)
        self.start_single_title_label.setObjectName(u"start_single_title_label")
        sizePolicy1.setHeightForWidth(self.start_single_title_label.sizePolicy().hasHeightForWidth())
        self.start_single_title_label.setSizePolicy(sizePolicy1)
        self.start_single_title_label.setMaximumSize(QSize(16777215, 22))
        self.start_single_title_label.setFont(font)
        self.start_single_title_label.setCursor(QCursor(Qt.IBeamCursor))
        self.start_single_title_label.setTextFormat(Qt.RichText)
        self.start_single_title_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.start_single_title_label.setWordWrap(True)
        self.start_single_title_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.start_single_title_label)

        self.start_single_content_label = QLabel(self.home_scrollAreaWidgetContents)
        self.start_single_content_label.setObjectName(u"start_single_content_label")
        sizePolicy1.setHeightForWidth(self.start_single_content_label.sizePolicy().hasHeightForWidth())
        self.start_single_content_label.setSizePolicy(sizePolicy1)
        self.start_single_content_label.setMaximumSize(QSize(16777215, 132))
        self.start_single_content_label.setFont(font)
        self.start_single_content_label.setCursor(QCursor(Qt.IBeamCursor))
        self.start_single_content_label.setTextFormat(Qt.RichText)
        self.start_single_content_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.start_single_content_label.setWordWrap(True)
        self.start_single_content_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.start_single_content_label)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.start_batch_title_label = QLabel(self.home_scrollAreaWidgetContents)
        self.start_batch_title_label.setObjectName(u"start_batch_title_label")
        sizePolicy1.setHeightForWidth(self.start_batch_title_label.sizePolicy().hasHeightForWidth())
        self.start_batch_title_label.setSizePolicy(sizePolicy1)
        self.start_batch_title_label.setMaximumSize(QSize(16777215, 22))
        self.start_batch_title_label.setFont(font)
        self.start_batch_title_label.setCursor(QCursor(Qt.IBeamCursor))
        self.start_batch_title_label.setTextFormat(Qt.RichText)
        self.start_batch_title_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.start_batch_title_label.setWordWrap(True)
        self.start_batch_title_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.start_batch_title_label)

        self.start_batch_content_label = QLabel(self.home_scrollAreaWidgetContents)
        self.start_batch_content_label.setObjectName(u"start_batch_content_label")
        sizePolicy1.setHeightForWidth(self.start_batch_content_label.sizePolicy().hasHeightForWidth())
        self.start_batch_content_label.setSizePolicy(sizePolicy1)
        self.start_batch_content_label.setMaximumSize(QSize(16777215, 88))
        self.start_batch_content_label.setFont(font)
        self.start_batch_content_label.setCursor(QCursor(Qt.IBeamCursor))
        self.start_batch_content_label.setTextFormat(Qt.RichText)
        self.start_batch_content_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.start_batch_content_label.setWordWrap(True)
        self.start_batch_content_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.start_batch_content_label)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.doc_label = QLabel(self.home_scrollAreaWidgetContents)
        self.doc_label.setObjectName(u"doc_label")
        sizePolicy1.setHeightForWidth(self.doc_label.sizePolicy().hasHeightForWidth())
        self.doc_label.setSizePolicy(sizePolicy1)
        self.doc_label.setMaximumSize(QSize(16777215, 22))
        self.doc_label.setFont(font)
        self.doc_label.setCursor(QCursor(Qt.IBeamCursor))
        self.doc_label.setTextFormat(Qt.RichText)
        self.doc_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.doc_label.setWordWrap(False)
        self.doc_label.setOpenExternalLinks(True)
        self.doc_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.doc_label)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.github_btn = QPushButton(self.home_scrollAreaWidgetContents)
        self.github_btn.setObjectName(u"github_btn")
        self.github_btn.setMinimumSize(QSize(100, 0))
        self.github_btn.setFont(font)
        self.github_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.github_btn)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_8 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.home_scrollArea.setWidget(self.home_scrollAreaWidgetContents)

        self.retranslateUi(homePageContent)

        QMetaObject.connectSlotsByName(homePageContent)
    # setupUi

    def retranslateUi(self, homePageContent):
        homePageContent.setWindowTitle(QCoreApplication.translate("homePageContent", u"homePageContent", None))
        self.home_icon.setText("")
        self.home_label.setText(QCoreApplication.translate("homePageContent", u"Home", None))
        self.home_title_label.setText(QCoreApplication.translate("homePageContent", u"Uni-CYPred", None))
        self.version_label.setText(QCoreApplication.translate("homePageContent", u"Version 1.0.0", None))
        self.home_icon_2.setText("")
        self.start_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p><span style=\" font-weight:600;\">Getting started</span></p></body></html>", None))
        self.start_single_title_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p><span style=\" font-weight:600;\">1. Single-Molecule Prediction</span></p></body></html>", None))
        self.start_single_content_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p>In &quot;Single-Molecule Prediction&quot; module, first input the <span style=\" font-weight:600;\">SMILES</span> string of the compound. Next, select the CYP450 isoforms you aim to predict in the <span style=\" font-weight:600;\">&quot;Select Prediction Models&quot;</span> section. Once you have made your selection, click the <span style=\" font-weight:600;\">&quot;START PREDICTION&quot;</span> button to initiate the prediction process. The prediction results will be displayed directly in the table below. Meanwhile, we also support downloading the results, just click the <span style=\" font-weight:600;\">&quot;Save Results&quot;</span> button below the table. Note that the downloaded file will contain all the data currently displayed in the table.</p></body></html>", None))
        self.start_batch_title_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p><span style=\" font-weight:600;\">2. Batch Prediction</span></p></body></html>", None))
        self.start_batch_content_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p>In &quot;Batch Prediction&quot; module, we provide support for predicting a collection of compounds simultaneously. However, the way to input compounds is different. You should click the <span style=\" font-weight:600;\">&quot;Browse&quot;</span> button to upload a file in txt or sdf format that contains the compounds. The subsequent steps are the same as those in &quot;Single-Molecule Prediction&quot; module.</p></body></html>", None))
        self.doc_label.setText(QCoreApplication.translate("homePageContent", u"<html><head/><body><p>If you're looking for a more detailed tutorial, please refer to our <a href=\"https://example.com/\"><span style=\" text-decoration: underline; color:#0055ff;\">documentation</span></a>.</p></body></html>", None))
        self.github_btn.setText(QCoreApplication.translate("homePageContent", u"GitHub", None))
    # retranslateUi

