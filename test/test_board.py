"""Tested functions

- set_cell
- clear_cell
"""

import unittest

from copy import deepcopy as copy
from utils import TEST_BOARD
from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(copy(TEST_BOARD))

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

    def test_set_cell_on_initial_cell_is_denied(self):
        self.assertFalse(
            self.board.set_cell(0, 0, 5),
            "Should not allow modifying an initial cell",
        )

    def test_clear_initial_cell_is_denied(self):
        self.assertFalse(
            self.board.clear_cell(0, 0),
            "Should not allow clearing an initial cell",
        )

    def test_clear_cell_valid(self):
        self.assertTrue(
            self.board.set_cell(3, 3, 5),
            "Should be possible to set an empty cell",
        )
        self.assertTrue(
            self.board.zeroes == 1,
            "Should have 1 zero now",
        )
        self.assertTrue(
            self.board.clear_cell(3, 3),
            "Should be possible to clear a set cell",
        )
        self.assertTrue(
            self.board.zeroes == 2,
            "Should have 2 zeroes now",
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
