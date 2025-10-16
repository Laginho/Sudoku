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


def has_nonzero_duplicate(vector: list[int]) -> bool:
    """Checks if a list contains duplicates of non zero values

    [0, 0, 3, 4, 5, 0, 3, 2, 1, 0, 0] -> True

    [0, 0, 3, 4, 5, 0, 6, 2, 1, 0, 0] -> False

    Args:
        vector: The list to check

    Returns:
        True if the list contains duplicates, False otherwise
    """
    st: set[int] = set()

    for item in vector:
        if item != 0 and item in st:
            return True
        st.add(item)

    return False


def count_zeroes(state: list[list[int]]) -> int:
    """Counts the number of zeroes in the given state

    Args:
        state: The board's current configuration

    Returns:
        The number of zeroes
    """
    return sum(row.count(0) for row in state)


def is_valid_input(entry: list[str]) -> bool:
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
