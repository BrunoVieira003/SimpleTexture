# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_pageyRkjxe.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(656, 563)
        self.verticalLayout = QVBoxLayout(SettingsPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 30, 0, 0)
        self.title = QLabel(SettingsPage)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.title)

        self.content = QFrame(SettingsPage)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.content)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"border: none;\n"
"}")
        self.groupBox.setFlat(True)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(40, 30, 0, 0)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.themes = QComboBox(self.groupBox)
        self.themes.setObjectName(u"themes")
        self.themes.setMinimumSize(QSize(120, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.themes)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 319, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.content)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"Form", None))
        self.title.setText(QCoreApplication.translate("SettingsPage", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Settings</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsPage", u"Appearance", None))
        self.label.setText(QCoreApplication.translate("SettingsPage", u"<html><head/><body><p>Theme:</p></body></html>", None))
    # retranslateUi

