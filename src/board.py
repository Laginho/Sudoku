"""Handles the board layout"""

import logic
import utils


class Board:
    """Handles the board layout

    The board is represented as a 2D array, with the zeroes representing
    empty spaces.

    Attributes:
        state: The board's current configuration
        zeroes: The number of zeroes in the board
    """

    def __init__(self, initial_state: list[list[int]] | None = None):
        if initial_state is not None:
            self.state: list[list[int]] = initial_state
            self.zeroes: int = utils.count_zeroes(self.state)
        else:
            self.state: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]
            self.zeroes: int = 81

    def is_solved(self):
        """Checks if the board is in a solved state"""

        return logic.check_board(self.state) and self.zeroes == 0
