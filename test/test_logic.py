import unittest

from utils import has_nonzero_duplicate
from logic import check_row, check_col, check_sqr, check_board


class TestUtils(unittest.TestCase):

    def test_has_nonzero_duplicate(self):
        # Case 1: A list with no duplicates
        no_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertFalse(
            has_nonzero_duplicate(no_duplicates),
            "Should be False for a list with no duplicates",
        )

        # Case 2: A list with duplicates
        with_duplicates = [1, 2, 3, 4, 5, 1, 7, 8, 9]
        self.assertTrue(
            has_nonzero_duplicate(with_duplicates),
            "Should be True for a list with duplicates",
        )

        # Case 3: A list with zeroes and no other duplicates
        with_zeroes = [0, 1, 2, 3, 0, 4, 5, 6, 7]
        self.assertFalse(
            has_nonzero_duplicate(with_zeroes),
            "Should be False as zeroes are ignored",
        )

        # Case 4: A list with zeroes and other duplicates
        with_zeroes_and_duplicates = [0, 1, 2, 1, 0, 4, 5, 6, 7]
        self.assertTrue(
            has_nonzero_duplicate(with_zeroes_and_duplicates),
            "Should be True for duplicates even with zeroes present",
        )

    def test_check_row(self):
        # Case 1: A list with no duplicates
        no_duplicates = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertTrue(
            check_row(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

        # Case 2: A list with duplicates
        with_duplicates = [[1, 2, 3, 4, 5, 1, 7, 8, 9]]
        self.assertFalse(
            check_row(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

        # Case 3: A list with zeroes and no other duplicates
        with_zeroes = [[1, 2, 3, 0, 5, 6, 0, 0, 9]]
        self.assertTrue(
            check_row(with_zeroes, 0),
            "Should be True as zeroes are ignored",
        )

        # Case 4: A list with zeroes and other duplicates
        with_zeroes_and_duplicates = [[1, 2, 3, 0, 5, 1, 0, 0, 9]]
        self.assertFalse(
            check_row(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_col(self):
        # Case 1: A list with no duplicates
        no_duplicates = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.assertTrue(
            check_col(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

        # Case 2: A list with duplicates
        with_duplicates = [[1], [2], [3], [4], [5], [6], [7], [8], [1]]
        self.assertFalse(
            check_col(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

        # Case 3: A list with zeroes and no other duplicates
        with_zeroes = [[1], [2], [3], [0], [5], [0], [0], [8], [9]]
        self.assertTrue(
            check_col(with_zeroes, 0),
            "Should be True as zeroes are ignored",
        )

        # Case 4: A list with zeroes and other duplicates
        with_zeroes_and_duplicates = [[1], [2], [3], [0], [0], [1], [7], [8], [9]]
        self.assertFalse(
            check_col(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_sqr(self):
        # Case 1: A list with no duplicates
        no_duplicates = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        self.assertTrue(
            check_sqr(no_duplicates, 0),
            "Should be True for a list with no duplicates",
        )

        # Case 2: A list with duplicates
        with_duplicates = [
            [1, 2, 3],
            [4, 5, 1],
            [7, 8, 9],
        ]

        self.assertFalse(
            check_sqr(with_duplicates, 0),
            "Should be False for a list with duplicates",
        )

        # Case 3: A list with zeroes and no other duplicates
        with_zeroes = [
            [1, 2, 3],
            [0, 5, 0],
            [0, 8, 9],
        ]

        self.assertTrue(
            check_sqr(with_zeroes, 0),
            "Should be False as zeroes are ignored",
        )

        # Case 4: A list with zeroes and other duplicates
        with_zeroes_and_duplicates = [
            [1, 2, 3],
            [0, 0, 4],
            [1, 8, 9],
        ]

        self.assertFalse(
            check_sqr(with_zeroes_and_duplicates, 0),
            "Should be False for duplicates even with zeroes present",
        )

    def test_check_board(self):
        # Case 1: A valid board state
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

        # Case 2: An invalid board state
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

        # Case 3: valid, but with zeroes
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
