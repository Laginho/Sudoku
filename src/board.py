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
        initial_cells: A set of tuples representing the fixed starting cells
    """

    def __init__(self, initial_state: list[list[int]] | None = None):
        """Initializes a new Sudoku board

        Args:
            initial_state: An optional 9x9 grid to start the puzzle.
                           If None, an empty 9x9 grid is created
        """

        self.initial_cells: set[tuple[int, int]] = set()

        if initial_state is not None:
            self.state: list[list[int]] = initial_state
            self.zeroes: int = utils.count_zeroes(self.state)
        else:
            self.state: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]
            self.zeroes: int = 81

    def is_solved(self) -> bool:
        """Checks if the board is in a solved state

        Returns:
            True if the board is valid and completely filled, False otherwise
        """

        return logic.check_board(self.state) and self.zeroes == 0

    def is_valid(self) -> bool:
        """Checks if the board is in a valid state

        Returns:
            True if the board state adheres to Sudoku rules, False otherwise
        """

        return logic.check_board(self.state)

    def set_cell(self, row: int, col: int, value: int) -> bool:
        """Sets a cell on the board to a given value

        The move is only applied if the cell is not an initial cell, is
        currently empty and the resulting board state remains valid.

        Args:
            row: The 0-indexed row of the cell (0-8)
            col: The 0-indexed column of the cell (0-8)
            value: The value to set the cell to (1-9)

        Returns:
            True if the cell was set successfully, False otherwise
        """

        if (row, col) in self.initial_cells:
            return False

        if self.state[row][col] != 0:
            return False

        self.state[row][col] = value

        if not self.is_valid():
            self.state[row][col] = 0
            return False

        self.zeroes -= 1
        return True

    def clear_cell(self, row: int, col: int) -> bool:
        """Clears a cell on the board

        The cell is only cleared if it is not an initial cell and is
        currently filled.

        Args:
            row: The 0-indexed row of the cell (0-8)
            col: The 0-indexed column of the cell (0-8)

        Returns:
            True if the cell was cleared successfully, False otherwise
        """

        if (row, col) in self.initial_cells:
            return False

        if self.state[row][col] == 0:
            return False

        self.state[row][col] = 0
        self.zeroes += 1
        return True

    def __str__(self) -> str:
        """The string representation of the board."""

        board = ""
        for i in range(9):
            for j in range(9):
                if self.state[i][j] == 0:
                    board += "  "
                else:
                    board += f"{self.state[i][j]} "
                if j in (2, 5):
                    board += "| "
            board += "\n"
            if i in (2, 5):
                board += "- - - + - - - + - - -\n"

        return board


if __name__ == "__main__":
    board = Board(utils.EXAMPLE_BOARD)
    print(board)
