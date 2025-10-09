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

    def is_valid(self):
        """Checks if the board is in a valid state"""

        return logic.check_board(self.state)

    def set_cell(self, row: int, col: int, value: int) -> bool:
        """Sets a cell on the board to a given value.

        Args:
            row: The row of the cell
            col: The column of the cell
            value: The value to set the cell to

        Returns:
            True if the cell was set successfully, False otherwise
        """
        if self.state[row][col] != 0:
            return False

        self.state[row][col] = value

        if not self.is_valid():
            self.state[row][col] = 0
            return False

        self.zeroes -= 1
        return True

    def clear_cell(self, row: int, col: int) -> bool:
        """Clears a cell on the board.

        Args:
            row: The row of the cell
            col: The column of the cell

        Returns:
            True if the cell was cleared successfully, False otherwise
        """
        if self.state[row][col] == 0:
            return False

        self.state[row][col] = 0
        self.zeroes += 1
        return True

    def __str__(self) -> str:
        return "\n".join("  ".join(str(x) for x in row) for row in self.state)


if __name__ == "__main__":
    board = Board(utils.EXAMPLE_BOARD)
    print(board)
