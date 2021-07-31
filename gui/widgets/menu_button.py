from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

class MenuButton(QPushButton):
    def __init__(self, text, min_size, icon, icon_size, callback,  text_color="#000000", padding=10, bg_hover="", bg_pressed=""):
        super().__init__()
        self.setMinimumWidth(min_size)
        self.setMinimumHeight(min_size)
        self.setFlat(True)
        self.setFont(QFont("Segoe", 12, 10))

        # Set icon
        self.setIcon(QIcon(f"gui\\images\\icons\\{icon}"))
        self.setIconSize(QSize(icon_size, icon_size))

        # Set text
        self.setText(text)

        # Set style
        self.padding = padding
        self.text_color = text_color
        self.bg_hover = bg_hover
        self.bg_pressed = bg_pressed

        self._reload_style()

        # Set callback
        self.clicked.connect(callback)
    
    def set_style_sheet(self, **kwargs):
        for k, v in kwargs.items():
            if k in ["text_color", "padding", "bg_hover", "bg_pressed"]:
                setattr(self, k, v)
        self._reload_style()
    
    def _reload_style(self):
        style = f"""
        QPushButton {{
            color: {self.text_color};
            padding-left: {self.padding}px;
            padding-right: {self.padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {self.bg_hover};
        }}
        QPushButton:pressed {{
            background-color: {self.bg_pressed};
        }}
        """

        self.setStyleSheet(style)
