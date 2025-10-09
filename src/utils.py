"""General utility constants and functions"""

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
