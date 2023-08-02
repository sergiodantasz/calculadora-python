from math import pow
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QMessageBox, QPushButton, QWidget

from display import Display
from info import Info
from utils import convert_to_number, is_num_or_dot, is_valid_number
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from window import Window


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
    def __init__(self, display: Display, info: Info, window: 'Window', parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.display = display
        self.info = info
        self.window = window
        self.__grid_mask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '=']
        ]
        self._equation_initial_value = 'CÁLCULO'
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equation_initial_value
        self._create_grid()
    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    
    def _create_grid(self) -> None:
        self.display.eq_pressed.connect(self._eq)
        self.display.bs_pressed.connect(self._backspace)
        self.display.esc_pressed.connect(self._clear)
        self.display.input_pressed.connect(self._insert_text_to_display)
        self.display.operator_pressed.connect(self._configure_left_op)
        for i, row in enumerate(self.__grid_mask):
            for j, button_text in enumerate(row):
                row_span = column_span = 1
                button = Button(button_text)
                if not is_num_or_dot(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configure_special_button(button)
                self.addWidget(button, i, j, row_span, column_span)
                slot = self._create_slot(
                    self._insert_text_to_display,
                    button_text
                )
                self._connect_button_clicked(button, slot)
    
    @staticmethod
    def _connect_button_clicked(button: Button, slot) -> None:
        button.clicked.connect(slot)
    
    @Slot()
    @staticmethod
    def _create_slot(function, *args, **kwargs):
        @Slot()
        def slot() -> None:
            function(*args, **kwargs)
        return slot
    
    def _configure_special_button(self, button: Button) -> None:
        button_text = button.text()
        if button_text == 'C':
            self._connect_button_clicked(button, self._clear)
        if button_text == 'D':
            self._connect_button_clicked(button, self.display.backspace)
        if button_text == 'N':
            self._connect_button_clicked(button, self._oppose_number)
        if button_text in '+-/*^':
            self._connect_button_clicked(
                button,
                self._create_slot(self._configure_left_op, button_text)
            )
        if button_text == '=':
            self._connect_button_clicked(button, self._eq)
    
    @Slot()
    def _insert_text_to_display(self, text: str) -> None:
        new_display_value = self.display.text() + text
        if not is_valid_number(new_display_value):
            return
        self.display.insert(text)
        self.display.setFocus()
    
    @Slot()
    def _oppose_number(self):
        display_text = self.display.text()
        if not is_valid_number(display_text):
            return
        number = convert_to_number(display_text) * (-1)
        self.display.setText(str(number))
    
    @Slot()
    def _clear(self) -> None:
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equation_initial_value
        self.display.clear()
        self.display.setFocus()
    
    @Slot()
    def _configure_left_op(self, text: str) -> None:
        display_text = self.display.text()
        self.display.clear()
        if not is_valid_number(display_text) and self._left is None:
            self._show_error('Cálculo incompleto.')
            return
        if self._left is None:
            self._left = convert_to_number(display_text)
        self._op = text
        self.equation = f'{self._left} {self._op} ?'
        self.display.setFocus()
    
    @Slot()
    def _eq(self) -> None:
        display_text = self.display.text()
        if not is_valid_number(display_text) or self._left is None:
            self._show_error('Cálculo incompleto.')
            return
        self._right = convert_to_number(display_text)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'ERRO'
        try:
            if '^' in self.equation and isinstance(self._left, (int, float)):
                result = pow(self._left, self._right)
            else:
                result = convert_to_number(eval(self.equation))
        except ZeroDivisionError:
            self._show_error('Impossível dividir por zero.')
        except OverflowError:
            self._show_error('Esse cálculo não pode ser realizado.')
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        if result == 'ERRO':
            self._left = None
        self.display.setFocus()
    
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()
    
    def _create_dialog(self, text: str) -> QMessageBox:
        msg_box = self.window.create_msg_box()
        msg_box.setText(text)
        return msg_box
    
    def _show_error(self, text: str) -> None:
        msg_box = self._create_dialog(text)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.setWindowTitle('ERRO')
        msg_box.exec()
        self.display.setFocus()

    def _show_info(self, text: str) -> None:
        msg_box = self._create_dialog(text)
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.setWindowTitle('INFORMAÇÃO')
        msg_box.exec()
        self.display.setFocus()
