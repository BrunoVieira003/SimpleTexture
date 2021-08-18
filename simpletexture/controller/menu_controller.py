import sys
import os
import json

from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.windows import MenuWindow
from model.general import GenericDatabase

class MenuWindowController:
    def __init__(self) -> None:
        super().__init__()

        self.window = MenuWindow()
        
        self.settings_data = GenericDatabase("data\\settings.json")

        # Themes
        for theme in os.listdir("assets\\themes"):
            theme = theme[:-5]
            self.window.add_theme(theme)
        theme_index = self.window.ui_settings.themes.findText(self.settings_data.get("theme").title())
        self.window.ui_settings.themes.setCurrentIndex(theme_index)
        
        self.set_window_theme(self.settings_data.get("theme"))

        # Binding
        self.window.ui_settings.themes.currentIndexChanged.connect(self.on_theme_changed)

    def on_theme_changed(self):
        self.settings_data.set("theme", self.window.ui_settings.themes.currentText().lower())
        self.set_window_theme(self.settings_data.get("theme"))
        
    
    def set_window_theme(self, theme):
        with open(f"assets\\themes\\{theme}.json", "r") as arc:
            theme_data = json.load(arc)
            self.window.set_theme(theme_data, theme)
    
    def show_window(self):
        self.window.show()