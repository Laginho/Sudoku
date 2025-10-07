"""General utility functions"""


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
