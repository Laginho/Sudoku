"""Tested functions

- set_cell
- clear_cell
"""

import unittest

from utils import EXAMPLE_BOARD
from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(EXAMPLE_BOARD)

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
