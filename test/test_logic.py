"""Tested functions

- check_row
- check_col
- check_sqr
- check_board
"""

import unittest

from logic import check_row, check_col, check_sqr, check_board


class TestLogic(unittest.TestCase):

    def test_check_row_no_duplicates(self):
        no_duplicates = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertTrue(
            check_row(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

    def test_check_row_with_duplicates(self):
        with_duplicates = [[1, 2, 3, 4, 5, 1, 7, 8, 9]]
        self.assertFalse(
            check_row(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

    def test_check_row_with_zeroes(self):
        with_zeroes = [[1, 2, 3, 0, 5, 6, 0, 0, 9]]
        self.assertTrue(
            check_row(with_zeroes, 0),
            "Should be True as zeroes are ignored",
        )

    def test_check_row_with_zeroes_and_duplicates(self):
        with_zeroes_and_duplicates = [[1, 2, 3, 0, 5, 1, 0, 0, 9]]
        self.assertFalse(
            check_row(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_col_no_duplicates(self):
        no_duplicates = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertTrue(
            check_col(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

    def test_check_col_with_duplicates(self):
        with_duplicates = [[1], [2], [3], [4], [5], [6], [7], [8], [1]]
        self.assertFalse(
            check_col(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

    def test_check_col_with_zeroes(self):
        with_zeroes = [[1], [2], [3], [0], [5], [0], [0], [8], [9]]
        self.assertTrue(
            check_col(with_zeroes, 0),
            "Should be True as zeroes are ignored",
        )

    def test_check_col_with_zeroes_and_duplicates(self):
        with_zeroes_and_duplicates = [[1], [2], [3], [0], [0], [1], [7], [8], [9]]
        self.assertFalse(
            check_col(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_sqr_no_duplicates(self):
        no_duplicates = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        self.assertTrue(
            check_sqr(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

    def test_check_sqr_with_duplicates(self):
        with_duplicates = [
            [1, 2, 3],
            [4, 5, 1],
            [7, 8, 9],
        ]

        self.assertFalse(
            check_sqr(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

    def test_check_sqr_with_zeroes(self):
        with_zeroes = [
            [1, 2, 3],
            [0, 5, 0],
            [0, 8, 9],
        ]

        self.assertTrue(
            check_sqr(with_zeroes, 0),
            "Should be True as zeroes are ignored",
        )

    def test_check_sqr_with_zeroes_and_duplicates(self):
        with_zeroes_and_duplicates = [
            [1, 2, 3],
            [0, 0, 4],
            [1, 8, 9],
        ]

        self.assertFalse(
            check_sqr(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_board_valid(self):
        valid_board = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]

        self.assertTrue(
            check_board(valid_board),
            "Should be True for a valid board state",
        )

    def test_check_board_invalid(self):
        invalid_board = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 1, 7, 8, 9, 6, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]

        self.assertFalse(
            check_board(invalid_board),
            "Should be False for an invalid board state",
        )

    def test_check_board_almost_valid(self):
        almost_valid_board = [
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

        self.assertTrue(
            check_board(almost_valid_board),
            "Should be True even with zeroes present",
        )


if __name__ == "__main__":
    unittest.main()
