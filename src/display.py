from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QWidget

from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.configure_style()

    def configure_style(self) -> None:
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(MINIMUM_WIDTH, BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
