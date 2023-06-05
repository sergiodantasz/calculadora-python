from PySide6.QtWidgets import QPushButton, QWidget

from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configure_style()
    
    def configure_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
