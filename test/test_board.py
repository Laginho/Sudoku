"""Tested functions

- set_cell
- clear_cell
"""

import unittest

from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        initial_state = [
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
        self.board = Board(initial_state)

    def test_set_cell_valid_move(self):
        self.assertTrue(
            self.board.set_cell(3, 3, 5),
            "Should be a valid move because the cell is empty",
        )

    def test_set_cell_already_filled(self):
        self.assertFalse(
            self.board.set_cell(0, 0, 6),
            "Should not be a valid move because the cell is already filled",
        )

    def test_set_cell_invalid_move(self):
        self.assertFalse(
            self.board.set_cell(3, 3, 6),
            "Should not be a valid move",
        )

    def test_clear_cell_valid(self):
        self.assertTrue(
            self.board.clear_cell(0, 0),
            "Should be possible to clear a set cell",
        )
        self.assertTrue(
            self.board.zeroes == 3,
            "Should have 3 zeroes now",
        )

    def test_clear_cell_invalid(self):
        self.assertFalse(
            self.board.clear_cell(3, 3),
            "Should not be a valid move because the cell is already empty",
        )
        self.assertTrue(
            self.board.zeroes == 2,
            "Should still have 2 zeroes",
        )


if __name__ == "__main__":
    unittest.main()
