from sys import argv

from PySide6.QtWidgets import QApplication

from styles import configure_theme
from window import Window


def main() -> None:
    app = QApplication(argv)
    window = Window()
    window.set_icon(app)
    configure_theme()
    window.adjust_fixed_size()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
