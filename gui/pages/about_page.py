# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_pageYVWrlV.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        if not AboutPage.objectName():
            AboutPage.setObjectName(u"AboutPage")
        AboutPage.resize(672, 647)
        self.verticalLayout = QVBoxLayout(AboutPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(AboutPage)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.title)

        self.content = QFrame(AboutPage)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 319, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.content)


        self.retranslateUi(AboutPage)

        QMetaObject.connectSlotsByName(AboutPage)
    # setupUi

    def retranslateUi(self, AboutPage):
        AboutPage.setWindowTitle(QCoreApplication.translate("AboutPage", u"Form", None))
        self.title.setText(QCoreApplication.translate("AboutPage", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">About</span></p></body></html>", None))
    # retranslateUi

