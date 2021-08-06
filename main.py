import sys
import os
import json

from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.windows.mainwindow import UI_MainWindow
from model.general import GenericDatabase

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.settings_data = GenericDatabase("data\\settings.json")

        # Themes
        for theme in os.listdir("gui\\themes"):
            theme = theme[:-5]
            self.ui.add_theme(theme)
        theme_index = self.ui.ui_settings.themes.findText(self.settings_data.get("theme").title())
        self.ui.ui_settings.themes.setCurrentIndex(theme_index)
        
        self.set_window_theme(self.settings_data.get("theme"))

        # Binding
        self.ui.ui_settings.themes.currentIndexChanged.connect(self.on_theme_changed)

    def on_theme_changed(self):
        self.settings_data.set("theme", self.ui.ui_settings.themes.currentText().lower())
        self.set_window_theme(self.settings_data.get("theme"))
        
    
    def set_window_theme(self, theme):
        with open(f"gui\\themes\\{theme}.json", "r") as arc:
            theme_data = json.load(arc)
            self.ui.set_theme(theme_data, theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())