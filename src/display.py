from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit, QWidget

from utils import is_empty, is_num_or_dot
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eq_pressed = Signal()
    bs_pressed = Signal()
    esc_pressed = Signal()
    input_pressed = Signal(str)
    operator_pressed = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._configure_style()

    def _configure_style(self) -> None:
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(MINIMUM_WIDTH, BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        is_enter = key in (KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal)
        is_backspace = key in (KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D)
        is_esc = key in (KEYS.Key_Escape, KEYS.Key_C)
        is_operator = key in (KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P)
        if is_enter or text == '=':
            self.eq_pressed.emit()
            return event.ignore()
        if is_backspace:
            self.bs_pressed.emit()
            return event.ignore()
        if is_esc:
            self.esc_pressed.emit()
            return event.ignore()
        if is_operator:
            if text.upper() == 'P':
                text = '^'
            self.operator_pressed.emit(text)
            return event.ignore()
        if is_empty(text):
            return event.ignore()
        if is_num_or_dot(text):
            self.input_pressed.emit(text)
            return event.ignore()
