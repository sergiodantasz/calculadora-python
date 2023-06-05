from sys import argv

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from display import Display
from info import Info
from styles import configure_theme
from variables import WINDOW_ICON_PATH
from window import Window


def main() -> None:
    app = QApplication(argv)
    window = Window()

    info = Info()
    info.setText('2.0 ^ 10.0 = 1024.0')
    window.add_widget_to_layout(info)

    display = Display()
    window.add_widget_to_layout(display)

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    configure_theme()
    window.adjust_fixed_size()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()
