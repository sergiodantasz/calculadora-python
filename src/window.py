from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from button import ButtonGrid
from display import Display
from info import Info
from variables import WINDOW_ICON_PATH


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
        self.button_grid = ButtonGrid(self.display, self.info, self)
        self.vertical_layout.addLayout(self.button_grid)
        self.setCentralWidget(self.central_widget)
    
    def adjust_fixed_size(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def add_widget_to_layout(self, widget: QWidget) -> None:
        self.vertical_layout.addWidget(widget)
    
    def set_icon(self, app: QApplication) -> None:
        icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(icon)
        app.setWindowIcon(icon)
    
    def create_msg_box(self):
        return QMessageBox(self)
