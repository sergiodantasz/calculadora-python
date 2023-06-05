from sys import argv

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from styles import configure_theme
from variables import WINDOW_ICON_PATH
from window import Window


def main() -> None:
    app = QApplication(argv)
    window = Window()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    configure_theme()
    window.adjust_fixed_size()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()
