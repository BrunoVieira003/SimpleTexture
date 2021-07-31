from PySide6.QtGui import QFont, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QRect, QSize, Qt

class MenuButton(QPushButton):
    def __init__(self, text, min_size, icon, icon_size, callback,  text_color="#000", icon_color="#000", bg_hover="", bg_pressed="", padding=10):
        super().__init__()
        self.setMinimumWidth(min_size)
        self.setMinimumHeight(min_size)
        self.setFlat(True)
        self.setFont(QFont("Segoe", 12, 10))

        # Set icon
        self.icon_path = f"gui\\images\\icons\\{icon}"
        self.icon_color = icon_color
        self.pixmap_icon = QPixmap(self.icon_path)
        self.icon_size = QSize(icon_size, icon_size)

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
            if k in ["text_color", "bg_hover", "bg_pressed", "icon_color", "padding"]:
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
    
    def paintEvent(self, event):
        # Paint default theme
        super().paintEvent(event)
        main_painter = QPainter()
        main_painter.begin(self)
        main_painter.setRenderHint(QPainter.Antialiasing)
        main_painter.setPen(Qt.NoPen)

        # Drawing icon
        icon = self.pixmap_icon
        self.setIcon(icon)
        self.setIconSize(self.icon_size)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self.icon_color)

        painter.end()
        main_painter.end()
