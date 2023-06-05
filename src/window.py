from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)
    
    def adjust_fixed_size(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def add_widget_to_layout(self, widget: QWidget) -> None:
        self.vertical_layout.addWidget(widget)
