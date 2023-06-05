from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget

from variables import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.configure_style()
    
    def configure_style(self) -> None:
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        self.setFont(font)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
