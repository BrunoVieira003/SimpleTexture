from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout, QWidget

# pages
from gui.pages.home_page import Ui_HomePage
from gui.pages.settings_page import Ui_SettingsPage
from gui.pages.about_page import Ui_AboutPage

# custom widgets
from gui.widgets.menu_button import MenuButton

import os
import json


class UI_MainWindow:
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # Set size of window
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        parent.setWindowTitle("Simple Texture")

        # Set central frame
        self.central_frame = QFrame()

        # Set main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)

        # left menu
        self.menu = QFrame()
        self.menu.setMaximumWidth(70)
        self.menu.setMinimumWidth(70)

        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setSpacing(0)
        self.menu_layout.setContentsMargins(0,0,0,0)

        
        self.toggle_button = MenuButton("Menu", 70, "menu_icon.svg", 50, self.toggle_menu) # Menu button
        self.home_button = MenuButton("Home", 70, "home_icon.svg", 50, lambda: self.change_page(0)) # Home button
        self.settings_button = MenuButton("Settings", 70, "settings_icon.svg", 50, lambda: self.change_page(1)) # Settings button
        self.about_button = MenuButton("About", 70, "info_icon.svg", 50, lambda: self.change_page(2)) # About button

        for button, icon in zip([self.home_button, self.settings_button, self.about_button], ["home", "settings", "info"]):
            button.setFlat(True)
            button.setMinimumHeight(70)
            button.setIcon(QIcon(f"gui\\images\\icons\\{icon}_icon.svg"))
            button.setIconSize(QSize(50, 50))

        self.menu_spacing = QSpacerItem(0, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menu_layout.addWidget(self.toggle_button)
        self.menu_layout.addWidget(self.home_button)
        self.menu_layout.addWidget(self.settings_button)
        self.menu_layout.addItem(self.menu_spacing)
        self.menu_layout.addWidget(self.about_button)

        # content
        self.content = QFrame()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(0,0,0,0)

        # Topbar
        self.topbar = QFrame()
        self.topbar.setMaximumHeight(70)
        self.topbar.setMinimumHeight(70)
        self.topbar_line = QFrame()
        self.topbar_line.setMinimumHeight(20)

        self.content_layout.addWidget(self.topbar)
        self.content_layout.addWidget(self.topbar_line)

        # Pages
        self.pages = QStackedWidget()

        self.home_page = QWidget()
        self.settings_page = QWidget()
        self.about_page = QWidget()

        self.ui_home = Ui_HomePage()
        self.ui_settings = Ui_SettingsPage()
        self.ui_about = Ui_AboutPage()

        for page, layout in zip([self.home_page, self.settings_page, self.about_page], [self.ui_home, self.ui_settings, self.ui_about]):
            layout.setupUi(page)
            self.pages.addWidget(page)

        self.content_layout.addWidget(self.pages)
        self.pages.setCurrentWidget(self.home_page)


        # Add widgets to main layout
        self.main_layout.addWidget(self.menu)
        self.main_layout.addWidget(self.content)
        
        parent.setCentralWidget(self.central_frame)
    
    def toggle_menu(self):
        menu_width = self.menu.width()
        if menu_width == 70:
            width = 150
        else:
            width = 70
        self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.setDuration(250)
        self.animation.start()
    
    def change_page(self, page_index):
        self.pages.setCurrentIndex(page_index)
    
    def set_theme(self, theme, theme_name):
        self.theme = theme
        
        # Basic layout
        self.central_frame.setStyleSheet(f"background-color: {self.theme['background']}")
        self.content.setStyleSheet(f"background-color: {self.theme['background']}")
        self.topbar.setStyleSheet(f"background-color: {self.theme['topbar']}")
        self.topbar_line.setStyleSheet(f"background-color: {self.theme['topbar_line']}")

        # Left menu
        self.menu.setStyleSheet(f"background-color: {self.theme['menu_background']}")
        for button in [self.toggle_button, self.home_button, self.settings_button, self.about_button]:
            button.set_style_sheet(bg_hover=self.theme['menu_button_hover'], bg_pressed=self.theme['menu_button_pressed'])
            button.set_style_sheet(text_color=self.theme['menu_text'], icon_color=self.theme['menu_icon_color'])

        # Pages
        self.ui_home.title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.home_page.setStyleSheet(f"color: {self.theme['text']}")

        self.ui_settings.title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.settings_page.setStyleSheet(f"color: {self.theme['text']}")

        self.ui_about.title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.about_page.setStyleSheet(f"color: {self.theme['text']}")

        # theme Combobox
        style = f"""
        QComboBox{{
            background-color: {self.theme['topbar']};
            border: none;
        }}
        """
        self.ui_settings.themes.setStyleSheet(style)
    
    def add_theme(self, theme):
        self.ui_settings.themes.addItem(theme.title())