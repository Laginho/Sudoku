"""Board validation logic.

Small collection of helpers used to validate rows, columns and 3x3 squares of a
Sudoku board. The primary entry point is :func:`check_board`.
"""

import utils


def check_row(state: list[list[int]], row: int) -> bool:
    """Checks if a given row configuration is valid

    Args:
        state: The board's current configuration
        row: The row to check

    Returns:
        True if the configuration is valid, False otherwise.
    """
    return not utils.has_nonzero_duplicate(state[row])


def check_col(state: list[list[int]], col: int) -> bool:
    """Checks if a given column configuration is valid

    Args:
        state: The board's current configuration
        col: The column to check

    Returns:
        True if the configuration is valid, False otherwise.

    Raises:
        ValueError: If the value for column is not valid
    """
    vector: list[int] = [state[i][col] for i in range(9)]

    return not utils.has_nonzero_duplicate(vector)


def check_sqr(state: list[list[int]], sqr: int) -> bool:
    """Checks if a given square configuration is valid

    Args:
        state: The board's current configuration
        sqr: The square to check. The squares are numbered
          as a cellphone numpad (0-8).

    Returns:
        True if the configuration is valid, False otherwise.

    Raises:
        ValueError: If the value for row is not valid
    """
    row: int = (sqr // 3) * 3
    col: int = (sqr % 3) * 3

    vector: list[int] = [
        state[i][j] for i in range(row, row + 3) for j in range(col, col + 3)
    ]

    return not utils.has_nonzero_duplicate(vector)


def check_board(state: list[list[int]]) -> bool:
    """Checks if the board is in a valid state

    Args:
        state: The board's current configuration

    Returns:
        True if the state is valid, False otherwise.
    """

    for i in range(9):
        if not check_row(state, i):
            return False
        if not check_col(state, i):
            return False
        if not check_sqr(state, i):
            return False

    return True
