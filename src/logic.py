"""Handles the logic for the board"""


class Logic:
    @staticmethod
    def check_row(state: list[list[int]], row: int) -> bool:
        """Checks if a given row configuration is valid

        Args:
            state: The board's current configuration
            row: The row to check

        Returns:
            True if the configuration is valid, False otherwise.

        Raises:
            ValueError: If the value for row is not valid
        """
        return True

    @staticmethod
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
        return True

    @staticmethod
    def check_sqr(state: list[list[int]], sqr: int) -> bool:
        """Checks if a given square configuration is valid

        Args:
            state: The board's current configuration
            sqr: The square to check. The squares are numbered
              as a cellphone numpad.

        Returns:
            True if the configuration is valid, False otherwise.

        Raises:
            ValueError: If the value for row is not valid
        """
        return True

    @staticmethod
    def is_solved(state: list[list[int]]) -> bool:
        """Checks if the board has been completed

        Args:
            state: The board's current configuration

        Returns:
            True if the board is solved, False otherwise.
        """

        rows: bool = True
        cols: bool = True
        sqrs: bool = True
        for i in range(9):
            if not Logic.check_row(state, i):
                rows = False
            if not Logic.check_col(state, i):
                cols = False
            if not Logic.check_sqr(state, i):
                sqrs = False

        return rows and cols and sqrs
