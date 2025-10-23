"""Constants for color definitions used throughout the Sudoku application.

This module provides RGBA color tuples (red, green, blue, alpha) for various UI
elements such as backgrounds, text, and highlights. All values are floats in the
range 0.0..1.0.

Constants:
    <COLOR_NAME>:
        An RGBA tuple with float components in the range 0.0..1.0.
"""

# Colors

RED: tuple[float, float, float, float] = (1, 0, 0, 1)
GREEN: tuple[float, float, float, float] = (0, 1, 0, 1)
BLUE: tuple[float, float, float, float] = (0, 0, 1, 1)
LBLUE: tuple[float, float, float, float] = (0.5, 0.7, 1, 1)
YELLOW: tuple[float, float, float, float] = (1, 1, 0, 1)
WHITE: tuple[float, float, float, float] = (1, 1, 1, 1)
BLACK: tuple[float, float, float, float] = (0, 0, 0, 1)
GRAY: tuple[float, float, float, float] = (0.5, 0.5, 0.5, 1)
LGRAY: tuple[float, float, float, float] = (0.75, 0.75, 0.75, 1)
DGRAY: tuple[float, float, float, float] = (0.2, 0.2, 0.2, 1)
SELECTED: tuple[float, float, float, float] = (0.6, 0.6, 1, 0.6)

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
