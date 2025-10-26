"""Board validation logic.

Small collection of helpers used to validate rows, columns and 3x3 squares of a
Sudoku board. The primary entry point is :func:`check_board`.
"""

import utils


def check_row(state: list[list[int]], row: int, num: int = 0) -> bool:
    """Checks if a given row configuration is valid

    If the user passes a number, it checks whether that number can be placed
    in the row without causing duplicates.

    Args:
        state: The board's current configuration
        row: The row to check
        num: Optional number to validate for placement in the row

    Returns:
        True if the configuration is valid, False otherwise.
    """
    if num == 0:
        return not utils.has_nonzero_duplicate(state[row])

    return state[row].count(num) == 0


def check_col(state: list[list[int]], col: int, num: int = 0) -> bool:
    """Checks if a given column configuration is valid

    If the user passes a number, it checks whether that number can be placed
    in the column without causing duplicates.

    Args:
        state: The board's current configuration
        col: The column to check
        num: Optional number to validate for placement in the column

    Returns:
        True if the configuration is valid, False otherwise.

    Raises:
        ValueError: If the value for column is not valid
    """
    vector: list[int] = [state[i][col] for i in range(9)]

    if num == 0:
        return not utils.has_nonzero_duplicate(vector)

    return vector.count(num) == 0


def check_sqr(state: list[list[int]], sqr: int, num: int = 0) -> bool:
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

    if num == 0:
        return not utils.has_nonzero_duplicate(vector)

    return vector.count(num) == 0


def check_move(state: list[list[int]], row: int, col: int, num: int) -> bool:
    """Checks whether placing a number in a 3x3 square would be valid.

    Args:
        state: 9x9 Sudoku board represented as a list of lists of ints.
        row: Row index (0-8) where the number is to be placed.
        col: Column index (0-8) where the number is to be placed.
        num: Number to validate (1-9).

    Returns:
        bool: True if the move is valid (no global duplicate of num and the
        specified 3x3 square remains valid), False otherwise.
    """
    sqr: int = (row // 3) * 3 + (col // 3)

    row: bool = check_row(state, row, num)
    col: bool = check_col(state, col, num)
    square: bool = check_sqr(state, sqr, num)

    return row and col and square


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
