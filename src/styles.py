from qdarktheme import setup_theme

from variables import PRIMARY_COLOR, QSS


def configure_theme() -> None:
    setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": PRIMARY_COLOR
            },
            "[light]": {
                "primary": PRIMARY_COLOR
            }
        },
        additional_qss=QSS
    )
