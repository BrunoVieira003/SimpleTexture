from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout
from gui.pages.ui_pages import Ui_pages
from gui.widgets.menu_button import MenuButton

import os
import json


class UI_MainWindow:
    def setup_ui(self, parent, theme="default"):
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
        self.ui_pages = Ui_pages()
        self.ui_pages.setupUi(self.pages)
        self.content_layout.addWidget(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.home)


        # Add widgets to main layout
        self.main_layout.addWidget(self.menu)
        self.main_layout.addWidget(self.content)
        
        parent.setCentralWidget(self.central_frame)
        
        #Themes Combobox
        for _theme in os.listdir("gui\\themes"):
            _theme = _theme[:-5]
            self.ui_pages.themes.addItem(_theme.title())
            fun = lambda: self.set_theme(self.ui_pages.themes.currentText().lower())
            self.ui_pages.themes.currentIndexChanged.connect(fun)

        # Add theme
        self.set_theme(theme)
    
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
    
    def set_theme(self, theme):
        with open(f"gui\\themes\\{theme}.json", "r") as arq:
            self.theme = json.load(arq)
        
        # Basic layout
        self.central_frame.setStyleSheet(f"background-color: {self.theme['background']}")
        self.content.setStyleSheet(f"background-color: {self.theme['background']}")
        self.topbar.setStyleSheet(f"background-color: {self.theme['topbar']}")
        self.topbar_line.setStyleSheet(f"background-color: {self.theme['topbar_line']}")

        # Left menu
        self.menu.setStyleSheet(f"background-color: {self.theme['menu_background']}")
        for button in [self.toggle_button, self.home_button, self.settings_button, self.about_button]:
            button.set_style_sheet(text_color=self.theme['menu_text'], bg_hover=self.theme['menu_button_hover'], bg_pressed=self.theme['menu_button_pressed'])

        # Pages
        self.ui_pages.home_title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.ui_pages.home.setStyleSheet(f"color: {self.theme['text']}")
        self.ui_pages.settings_title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.ui_pages.settings.setStyleSheet(f"color: {self.theme['text']}")
        self.ui_pages.about_title.setStyleSheet(f"color: {self.theme['page_title']}")
        self.ui_pages.about.setStyleSheet(f"color: {self.theme['text']}")

        # theme Combobox
        style = f"""
        QComboBox{{
            background-color: {self.theme['topbar']};
        selection-background-color: {self.theme['topbar']};
        border: none;
        }}
        """
        self.ui_pages.themes.setStyleSheet(style)