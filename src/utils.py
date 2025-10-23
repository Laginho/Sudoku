# pylint: disable=C0103

"""Utility helpers used across the project.

This module contains several small helper functions for validating and
manipulating Sudoku board data structures.

Functions:
    has_nonzero_duplicate: Detect duplicates among non-zero values in a list.
    count_zeroes: Count the empty cells on a board.
    get_initial_cells: Return coordinates for initially filled cells.
    is_valid_input: Validate terminal input for moves.
    parse_puzzle_string: Convert an 81-char puzzle string to a 9x9 grid.
"""


def has_nonzero_duplicate(vector: list[int]) -> bool:
    """Checks if a list contains duplicates of non zero values

    [0, 0, 3, 4, 5, 0, 3, 2, 1, 0, 0] -> True (list[2] == list[6] == 3)

    [0, 0, 3, 4, 5, 0, 6, 2, 1, 0, 0] -> False

    Args:
        vector: The list to check

    Returns:
        True if the list contains duplicates, False otherwise
    """
    counted_elements: set[int] = set()

    for element in vector:
        if element in counted_elements and element != 0:
            return True

        counted_elements.add(element)

    return False


def count_zeroes(state: list[list[int]]) -> int:
    """Counts the number of zeroes in the given state

    Args:
        state: The board's current configuration

    Returns:
        The number of zeroes
    """

    return sum(row.count(0) for row in state)


def get_initial_cells(state: list[list[int]]) -> set[tuple[int, int]]:
    """Returns a set of protected cells of the initial board state

    Args:
        state(list[list[int]]): The initial board state.

    Returns:
        set: The coordinates for all initially filled cells.
    """

    initial_cells: set[tuple[int, int]] = set()

    for row in range(9):
        for col in range(9):
            if state[row][col] != 0:
                initial_cells.add((row, col))

    return initial_cells


def is_valid_input(entry: list[str]) -> bool:
    """Checks if the raw string input from the terminal is a valid move format

    Expects exactly three elements (row, column, value), all of which must be
    digits between 1 and 9 (inclusive).

    Args:
        entry: A list of string segments from the user input
        (e.g., ['3', '4', '5'])

    Returns:
        bool: True if the input is valid, False otherwise
    """

    interval = range(1, 10)
    if len(entry) != 3:
        return False
    if not all(entry[i].isdigit() for i in range(3)):
        return False

    row: int = int(entry[0])
    col: int = int(entry[1])
    val: int = int(entry[2])

    if any(item not in interval for item in [row, col, val]):
        return False

    return True


def parse_puzzle_string(puzzle_str: str) -> list[list[int]]:
    """Converts an 81-character string into a 9x9 matrix of integers.

    Args:
        puzzle_str: The 81-character string representing the puzzle
                    (0-9, where 0 is an empty cell).

    Returns:
        A 9x9 list of lists of integers, or an empty 2d list if the input
        string is invalid (wrong length or contains non-digits).
    """

    if len(puzzle_str) != 81 or not puzzle_str.isdigit():
        return [[]]

    grid: list[list[int]] = []

    try:
        for i in range(9):
            row_str = puzzle_str[i * 9 : (i + 1) * 9]
            row = [int(char) for char in row_str]
            grid.append(row)

        return grid

    except ValueError:
        return [[]]


def rgb_to_kivy(color: tuple[int, int, int]) -> tuple[float, float, float, float]:
    """Converts an RGB color tuple to the Kivy RGBA format up to two decimal places.

    You can use it like this:

        color = (137, 0, 0)
        kivy_color = Color.rgb_to_kivy(color)

        # (0.54, 0.0, 0.0, 1.0)

    Args:
        color: A tuple representing the RGB color.

    Returns:
        A tuple representing the Kivy RGBA format.
    """

    r = round(color[0] / 255, 2)
    g = round(color[1] / 255, 2)
    b = round(color[2] / 255, 2)

    return (r, g, b, 1.0)


def hex_to_kivy(color: str | int) -> tuple[float, float, float, float]:
    """Converts a hex color to the Kivy RGBA format up to two decimal places.

    You can use it like this:

        color: str = "#FF5733"
        color2: int = 0xFF5733
        kivy_color = Color.hex_to_kivy(color)
        kivy_color2 = Color.hex_to_kivy(color2)

        # color == (1.0, 0.34, 0.2, 1.0)
        # color2 == (1.0, 0.34, 0.2, 1.0)

    Args:
        color: A string, or int, representing the hex color.

    Returns:
        A tuple representing the Kivy RGBA format.
    """

    if isinstance(color, int):
        color = f"#{color:06X}"
    elif color.startswith("#"):
        color = color[1:]

    r = round(int(color[0:2], 16) / 255, 2)
    g = round(int(color[2:4], 16) / 255, 2)
    b = round(int(color[4:6], 16) / 255, 2)

    return (r, g, b, 1.0)
