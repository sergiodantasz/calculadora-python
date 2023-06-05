from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from button import ButtonGrid
from display import Display
from info import Info


class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.info = Info()
        self.add_widget_to_layout(self.info)
        self.display = Display()
        self.add_widget_to_layout(self.display)
        self.button_grid = ButtonGrid(self.display, self.info)
        self.vertical_layout.addLayout(self.button_grid)
        self.setCentralWidget(self.central_widget)
    
    def adjust_fixed_size(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def add_widget_to_layout(self, widget: QWidget) -> None:
        self.vertical_layout.addWidget(widget)
