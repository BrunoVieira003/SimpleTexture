# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesrbXnlX.ui'
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
        self.verticalLayout.setContentsMargins(48, 48, 0, 0)
        self.home_title = QLabel(self.home)
        self.home_title.setObjectName(u"home_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_title.sizePolicy().hasHeightForWidth())
        self.home_title.setSizePolicy(sizePolicy)
        self.home_title.setMargin(0)

        self.verticalLayout.addWidget(self.home_title)

        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 521, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.frame)

        pages.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_2 = QVBoxLayout(self.settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(48, 48, 0, 0)
        self.settings_title = QLabel(self.settings)
        self.settings_title.setObjectName(u"settings_title")
        sizePolicy.setHeightForWidth(self.settings_title.sizePolicy().hasHeightForWidth())
        self.settings_title.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.settings_title)

        self.frame_2 = QFrame(self.settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.appearance = QGroupBox(self.frame_2)
        self.appearance.setObjectName(u"appearance")
        sizePolicy.setHeightForWidth(self.appearance.sizePolicy().hasHeightForWidth())
        self.appearance.setSizePolicy(sizePolicy)
        self.appearance.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(14)
        self.appearance.setFont(font)
        self.appearance.setStyleSheet(u"QGroupBox{\n"
"border: none;\n"
"}")
        self.appearance.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.appearance.setFlat(True)
        self.formLayout = QFormLayout(self.appearance)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(40, 30, 0, 0)
        self.label = QLabel(self.appearance)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.themes = QComboBox(self.appearance)
        self.themes.setObjectName(u"themes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.themes.sizePolicy().hasHeightForWidth())
        self.themes.setSizePolicy(sizePolicy1)
        self.themes.setMinimumSize(QSize(120, 0))
        self.themes.setFont(font1)
        self.themes.setStyleSheet(u"")
        self.themes.setInsertPolicy(QComboBox.NoInsert)
        self.themes.setIconSize(QSize(16, 16))
        self.themes.setPlaceholderText(u"")
        self.themes.setFrame(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.themes)


        self.verticalLayout_5.addWidget(self.appearance)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        pages.addWidget(self.settings)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_3 = QVBoxLayout(self.about)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(48, 48, 0, 0)
        self.about_title = QLabel(self.about)
        self.about_title.setObjectName(u"about_title")
        sizePolicy.setHeightForWidth(self.about_title.sizePolicy().hasHeightForWidth())
        self.about_title.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.about_title)

        self.frame_3 = QFrame(self.about)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.author = QLabel(self.frame_3)
        self.author.setObjectName(u"author")
        sizePolicy.setHeightForWidth(self.author.sizePolicy().hasHeightForWidth())
        self.author.setSizePolicy(sizePolicy)
        self.author.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.author)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_3)

        pages.addWidget(self.about)

        self.retranslateUi(pages)

        pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(pages)
    # setupUi

    def retranslateUi(self, pages):
        pages.setWindowTitle(QCoreApplication.translate("pages", u"StackedWidget", None))
        self.home_title.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Home</span></p></body></html>", None))
        self.settings_title.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Settings</span></p></body></html>", None))
        self.appearance.setTitle(QCoreApplication.translate("pages", u"Appearance", None))
        self.label.setText(QCoreApplication.translate("pages", u"Theme:", None))
        self.themes.setCurrentText("")
        self.about_title.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">About</span></p></body></html>", None))
        self.author.setText(QCoreApplication.translate("pages", u"<html><head/><body><p><span style=\" font-size:12pt;\">Created by Amenduim</span></p></body></html>", None))
    # retranslateUi

