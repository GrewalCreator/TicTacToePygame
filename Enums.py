from PygameSetUp import pg
from enum import Enum


# Define Color Values
class Color(Enum):
    BLACK = pg.Color(0, 0, 0)
    WHITE = pg.Color(255, 255, 255)
    RED = pg.Color(255, 0, 0)
    GREEN = pg.Color(0, 255, 0)
    BLUE = pg.Color(0, 0, 255)
    BG = pg.Color(28, 170, 156)
    LINE = pg.Color(23, 145, 135)
