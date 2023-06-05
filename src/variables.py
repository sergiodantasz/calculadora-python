from pathlib import Path

ROOT_DIR = Path(__file__).parent
ASSETS_DIR = ROOT_DIR / 'assets'
IMG_DIR = ASSETS_DIR / 'img'
WINDOW_ICON_PATH = IMG_DIR / 'icon.png'

BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500

PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'

QSS = f"""\
QPushButton[cssClass="specialButton"] {{
    color: #fff;
    background-color: {PRIMARY_COLOR}
}}
QPushButton[cssClass="specialButton"]:hover {{
    color: #fff;
    background-color: {DARKER_PRIMARY_COLOR}
}}
QPushButton[cssClass="specialButton"]:pressed {{
    color: #fff;
    background-color: {DARKEST_PRIMARY_COLOR}
}}\
"""
