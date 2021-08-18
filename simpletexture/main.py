import sys

import PySide6
from PySide6.QtWidgets import QApplication
import controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_controller = controller.MenuWindowController()
    menu_controller.show_window()
    sys.exit(app.exec())