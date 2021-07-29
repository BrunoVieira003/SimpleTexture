from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout
from gui.pages.ui_pages import Ui_pages

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

        self.toggle_button = QPushButton(text="Menu")
        self.toggle_button.setFlat(True)
        self.toggle_button.setMinimumHeight(70)

        self.menu_spacing = QSpacerItem(0, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menu_layout.addWidget(self.toggle_button)
        self.menu_layout.addItem(self.menu_spacing)

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

        # Bind buttons
        self.toggle_button.clicked.connect(self.toggle_menu)

        # Add theme
        self.set_theme(theme)
    
    def toggle_menu(self):
        button_width = self.menu.width()
        if button_width == 70:
            width = 240
        else:
            width = 70
        self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
        self.animation.setStartValue(button_width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.setDuration(250)
        self.animation.start()
    
    def set_theme(self, theme):
        with open(f"gui\\themes\\{theme}.json", "r") as arq:
            self.theme = json.load(arq)
        self.central_frame.setStyleSheet(f"background-color: {self.theme['background']}")
        self.content.setStyleSheet(f"background-color: {self.theme['background']}")
        self.menu.setStyleSheet(f"background-color: {self.theme['menu_background']}")
        self.toggle_button.setStyleSheet("border: none; background-color: #ffffff")
        self.topbar.setStyleSheet(f"background-color: {self.theme['topbar']}")
        self.topbar_line.setStyleSheet(f"background-color: {self.theme['topbar_line']}")