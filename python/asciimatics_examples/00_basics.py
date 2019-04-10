# pip install asciimatics

# pip install windows-curses
# or
# pip install pypiwin32 

# https://asciimatics.readthedocs.io/en/stable/intro.html
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, BannerText
from asciimatics.renderers import FigletText

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ASCIIMATICS", font='big'),
            screen.height // 2 - 8),
        BannerText(
            screen,
            FigletText("ROCKS!", font='big'),
            screen.height // 2 + 3,
            Screen.COLOUR_CYAN,
            Screen.COLOUR_BLACK),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)
