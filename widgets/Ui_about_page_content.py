# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_page_content.ui'
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

class Ui_aboutPageContent(object):
    def setupUi(self, aboutPageContent):
        if not aboutPageContent.objectName():
            aboutPageContent.setObjectName(u"aboutPageContent")
        aboutPageContent.resize(864, 642)
        aboutPageContent.setMinimumSize(QSize(864, 642))
        aboutPageContent.setMaximumSize(QSize(864, 642))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        aboutPageContent.setFont(font)
        aboutPageContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.about_scrollArea = QScrollArea(aboutPageContent)
        self.about_scrollArea.setObjectName(u"about_scrollArea")
        self.about_scrollArea.setGeometry(QRect(0, 0, 864, 642))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_scrollArea.sizePolicy().hasHeightForWidth())
        self.about_scrollArea.setSizePolicy(sizePolicy)
        self.about_scrollArea.setFrameShape(QFrame.NoFrame)
        self.about_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.about_scrollArea.setWidgetResizable(True)
        self.about_scrollAreaWidgetContents = QWidget()
        self.about_scrollAreaWidgetContents.setObjectName(u"about_scrollAreaWidgetContents")
        self.about_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 646))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.about_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.about_scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.about_scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 0, 40, 0)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.about_headline_hlay = QHBoxLayout()
        self.about_headline_hlay.setSpacing(6)
        self.about_headline_hlay.setObjectName(u"about_headline_hlay")
        self.about_icon = QLabel(self.about_scrollAreaWidgetContents)
        self.about_icon.setObjectName(u"about_icon")
        self.about_icon.setMaximumSize(QSize(20, 20))
        self.about_icon.setPixmap(QPixmap(u":/icons/icons/Bootstrap-Bootstrap-Bootstrap-info-circle.ico"))
        self.about_icon.setScaledContents(True)
        self.about_icon.setAlignment(Qt.AlignCenter)

        self.about_headline_hlay.addWidget(self.about_icon)

        self.about_label = QLabel(self.about_scrollAreaWidgetContents)
        self.about_label.setObjectName(u"about_label")
        sizePolicy1.setHeightForWidth(self.about_label.sizePolicy().hasHeightForWidth())
        self.about_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.about_label.setFont(font1)
        self.about_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.about_headline_hlay.addWidget(self.about_label)


        self.verticalLayout.addLayout(self.about_headline_hlay)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.about_title_label = QLabel(self.about_scrollAreaWidgetContents)
        self.about_title_label.setObjectName(u"about_title_label")
        sizePolicy1.setHeightForWidth(self.about_title_label.sizePolicy().hasHeightForWidth())
        self.about_title_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.about_title_label.setFont(font2)
        self.about_title_label.setFrameShape(QFrame.NoFrame)
        self.about_title_label.setFrameShadow(QFrame.Plain)
        self.about_title_label.setTextFormat(Qt.PlainText)
        self.about_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.about_title_label)

        self.version_label = QLabel(self.about_scrollAreaWidgetContents)
        self.version_label.setObjectName(u"version_label")
        sizePolicy1.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy1)
        self.version_label.setFont(font)
        self.version_label.setCursor(QCursor(Qt.IBeamCursor))
        self.version_label.setMouseTracking(True)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.version_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.version_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.intro_label = QLabel(self.about_scrollAreaWidgetContents)
        self.intro_label.setObjectName(u"intro_label")
        sizePolicy1.setHeightForWidth(self.intro_label.sizePolicy().hasHeightForWidth())
        self.intro_label.setSizePolicy(sizePolicy1)
        self.intro_label.setMaximumSize(QSize(16777215, 44))
        self.intro_label.setFont(font)
        self.intro_label.setCursor(QCursor(Qt.IBeamCursor))
        self.intro_label.setTextFormat(Qt.RichText)
        self.intro_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.intro_label.setWordWrap(True)
        self.intro_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.intro_label)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.copy_label = QLabel(self.about_scrollAreaWidgetContents)
        self.copy_label.setObjectName(u"copy_label")
        sizePolicy1.setHeightForWidth(self.copy_label.sizePolicy().hasHeightForWidth())
        self.copy_label.setSizePolicy(sizePolicy1)
        self.copy_label.setMaximumSize(QSize(16777215, 44))
        self.copy_label.setFont(font)
        self.copy_label.setCursor(QCursor(Qt.IBeamCursor))
        self.copy_label.setTextFormat(Qt.RichText)
        self.copy_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.copy_label.setWordWrap(True)
        self.copy_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.copy_label)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.license_label = QLabel(self.about_scrollAreaWidgetContents)
        self.license_label.setObjectName(u"license_label")
        sizePolicy1.setHeightForWidth(self.license_label.sizePolicy().hasHeightForWidth())
        self.license_label.setSizePolicy(sizePolicy1)
        self.license_label.setMaximumSize(QSize(16777215, 66))
        self.license_label.setFont(font)
        self.license_label.setCursor(QCursor(Qt.IBeamCursor))
        self.license_label.setFocusPolicy(Qt.NoFocus)
        self.license_label.setTextFormat(Qt.RichText)
        self.license_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.license_label.setWordWrap(True)
        self.license_label.setOpenExternalLinks(True)
        self.license_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.license_label)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.contact_label = QLabel(self.about_scrollAreaWidgetContents)
        self.contact_label.setObjectName(u"contact_label")
        sizePolicy1.setHeightForWidth(self.contact_label.sizePolicy().hasHeightForWidth())
        self.contact_label.setSizePolicy(sizePolicy1)
        self.contact_label.setMaximumSize(QSize(16777215, 44))
        self.contact_label.setFont(font)
        self.contact_label.setCursor(QCursor(Qt.IBeamCursor))
        self.contact_label.setTextFormat(Qt.RichText)
        self.contact_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.contact_label.setWordWrap(True)
        self.contact_label.setOpenExternalLinks(True)
        self.contact_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.contact_label)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.thanks_label = QLabel(self.about_scrollAreaWidgetContents)
        self.thanks_label.setObjectName(u"thanks_label")
        sizePolicy1.setHeightForWidth(self.thanks_label.sizePolicy().hasHeightForWidth())
        self.thanks_label.setSizePolicy(sizePolicy1)
        self.thanks_label.setMaximumSize(QSize(16777215, 44))
        self.thanks_label.setFont(font)
        self.thanks_label.setCursor(QCursor(Qt.IBeamCursor))
        self.thanks_label.setTextFormat(Qt.RichText)
        self.thanks_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.thanks_label.setWordWrap(True)
        self.thanks_label.setOpenExternalLinks(True)
        self.thanks_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.thanks_label)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.report_btn = QPushButton(self.about_scrollAreaWidgetContents)
        self.report_btn.setObjectName(u"report_btn")
        self.report_btn.setMinimumSize(QSize(150, 0))
        self.report_btn.setFont(font)
        self.report_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.report_btn)

        self.update_btn = QPushButton(self.about_scrollAreaWidgetContents)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(180, 0))
        self.update_btn.setFont(font)
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.update_btn)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.about_scrollArea.setWidget(self.about_scrollAreaWidgetContents)

        self.retranslateUi(aboutPageContent)

        QMetaObject.connectSlotsByName(aboutPageContent)
    # setupUi

    def retranslateUi(self, aboutPageContent):
        aboutPageContent.setWindowTitle(QCoreApplication.translate("aboutPageContent", u"aboutPageContent", None))
        self.about_icon.setText("")
        self.about_label.setText(QCoreApplication.translate("aboutPageContent", u"About", None))
        self.about_title_label.setText(QCoreApplication.translate("aboutPageContent", u"Uni-CYPred", None))
        self.version_label.setText(QCoreApplication.translate("aboutPageContent", u"Version 1.0.0", None))
        self.intro_label.setText(QCoreApplication.translate("aboutPageContent", u"Uni-CYPred is an open-source software specifically designed for predicting potential inhibitors of Cytochrome P450 enzymes, based on our existing best models.", None))
        self.copy_label.setText(QCoreApplication.translate("aboutPageContent", u"Copyright &copy; 2023 Laboratory of Molecular Modeling and Design, School of Pharmacy, East China University of Science and Technology. All rights reserved.", None))
        self.license_label.setText(QCoreApplication.translate("aboutPageContent", u"<html><head/><body><p>License: This software is powered by the PySide6 library (LGPLv3) and is released under the BSD 3-Clause License. Please see <a href=\"https://github.com/dreamlessdrugs/Uni-CYPred\"><span style=\" text-decoration: underline; color:#0055ff;\">https://github.com/dreamlessdrugs/Uni-CYPred</span></a> for more details about Uni-CYPred licenses.</p></body></html>", None))
        self.contact_label.setText(QCoreApplication.translate("aboutPageContent", u"<html><head/><body><p>Developed by Xiang Li and Prof. Weihua Li. Contact us by Email: <a href=\"mailto:whli@ecust.edu.cn\"><span style=\" text-decoration: underline; color:#0055ff;\">whli@ecust.edu.cn</span></a>. See <a href=\"http://lmmd.ecust.edu.cn/\"><span style=\" text-decoration: underline; color:#0055ff;\">LMMD</span></a> for more information about our laboratory.</p></body></html>", None))
        self.thanks_label.setText(QCoreApplication.translate("aboutPageContent", u"<html><head/><body><p>We would also like to express our gratitude to scikit-learn, RDKit, and DeepChem for making this software possible.</p></body></html>", None))
        self.report_btn.setText(QCoreApplication.translate("aboutPageContent", u"Report issues", None))
        self.update_btn.setText(QCoreApplication.translate("aboutPageContent", u"Check for updates", None))
    # retranslateUi

