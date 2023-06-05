from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton, QWidget

from display import Display
from utils import is_num_or_dot
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self._configure_style()
    
    def _configure_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.display = display
        self._grid_mask = [
            ['C', '⌫', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        self._create_grid()
    
    def _create_grid(self) -> None:
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                row_span = column_span = 1
                button = Button(button_text)
                if not is_num_or_dot(button_text):
                    button.setProperty('cssClass', 'specialButton')
                if i == 4:
                    if j == 0:
                        column_span = 2
                    else:
                        j += 1
                self.addWidget(button, i, j, row_span, column_span)
                button_slot = self._create_button_slot(
                    button,
                    self._insert_button_text_to_display
                )
                button.clicked.connect(button_slot)
    
    @staticmethod
    def _create_button_slot(button: Button, function):
        @Slot()
        def slot() -> None:
            function(button)
        return slot
    
    def _insert_button_text_to_display(self, button: Button) -> None:
        pass
