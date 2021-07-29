# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesLQdibr.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_pages(object):
    def setupUi(self, pages):
        if not pages.objectName():
            pages.setObjectName(u"pages")
        pages.resize(781, 624)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout = QVBoxLayout(self.home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(27, 27, 27);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(32)

        self.verticalLayout.addWidget(self.label)

        pages.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_2 = QVBoxLayout(self.settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.frame_2.setStyleSheet(u"background-color: rgb(27, 27, 27);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_2 = QLabel(self.settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.label_2.setMargin(32)

        self.verticalLayout_2.addWidget(self.label_2)

        pages.addWidget(self.settings)

        self.retranslateUi(pages)

        QMetaObject.connectSlotsByName(pages)
    # setupUi

    def retranslateUi(self, pages):
        pages.setWindowTitle(QCoreApplication.translate("pages", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Home</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Settings</span></p></body></html>", None))
    # retranslateUi

