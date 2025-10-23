"""Constants for example Sudoku boards and application colors."""

import utils

# Game elements

EXAMPLE_BOARD: list[list[int]] = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 0, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 0, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

TEST_BOARD = EXAMPLE_BOARD

# Colors

RED: tuple[float, float, float, float] = utils.hex_to_kivy("#FF0000")
GREEN: tuple[float, float, float, float] = utils.hex_to_kivy("#00FF00")
BLUE: tuple[float, float, float, float] = utils.hex_to_kivy("#0000FF")
LBLUE: tuple[float, float, float, float] = utils.hex_to_kivy("#80B3FF")
YELLOW: tuple[float, float, float, float] = utils.hex_to_kivy("#FFFF00")
WHITE: tuple[float, float, float, float] = utils.hex_to_kivy("#FFFFFF")
BLACK: tuple[float, float, float, float] = utils.hex_to_kivy("#000000")
GRAY: tuple[float, float, float, float] = utils.hex_to_kivy("#808080")
LGRAY: tuple[float, float, float, float] = utils.hex_to_kivy("#BFBFBF")
LLGRAY: tuple[float, float, float, float] = utils.hex_to_kivy("#D9D9D9")
DGRAY: tuple[float, float, float, float] = utils.hex_to_kivy("#333333")
BROWN: tuple[float, float, float, float] = utils.hex_to_kivy("#CC994D")
SELECTED: tuple[float, float, float, float] = utils.hex_to_kivy("#9999FF")
KINDLE_BG: tuple[float, float, float, float] = utils.hex_to_kivy("#FBF0D9")
DEFAULT: tuple[float, float, float, float] = KINDLE_BG
