"""Project-level configuration for the Sudoku application.

This module provides a minimal set of configuration constants used across the
project such as the application window size and a canonical 9x9 example board.

Constants:
    WINDOW_SIZE (tuple[int, int]): Default application window size as
        (width, height) in pixels.
    EXAMPLE_BOARD (list[list[int]]): Example 9x9 Sudoku board used for
        testing and debugging.
    TEST_BOARD (list[list[int]]): Alias of ``EXAMPLE_BOARD`` for convenience.
"""

from kivy.metrics import sp

# default: 405x720
DEFAULT = (405, 720)
MODE1 = (540, 960)
MODE2 = (675, 1200)
PHONE = (1080, 1920)
# WINDOW_SIZE: tuple[int, int] = PHONE

NUMBER_SIZE: int = sp(30)
