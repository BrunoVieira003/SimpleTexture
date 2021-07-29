import sys
from typing import Optional

from PySide6.QtCore import QPropertyAnimation
from gui.windows.mainwindow import UI_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self, theme="default")

        self.show()
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())