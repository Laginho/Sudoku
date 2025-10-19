"""General utility constants and functions"""

from dataclasses import dataclass

WINDOW_SIZE: tuple[int, int] = (405, 720)

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


@dataclass
class Colors:
    """Color constants"""

    RED: tuple[float, float, float, float] = (1, 0, 0, 1)
    GREEN: tuple[float, float, float, float] = (0, 1, 0, 1)
    BLUE: tuple[float, float, float, float] = (0, 0, 1, 1)
    YELLOW: tuple[float, float, float, float] = (1, 1, 0, 1)
    WHITE: tuple[float, float, float, float] = (1, 1, 1, 1)
    BLACK: tuple[float, float, float, float] = (0, 0, 0, 1)
    GRAY: tuple[float, float, float, float] = (0.5, 0.5, 0.5, 1)
    DGRAY: tuple[float, float, float, float] = (0.2, 0.2, 0.2, 1)
    SELECTED: tuple[float, float, float, float] = (0.6, 0.6, 1, 0.6)
