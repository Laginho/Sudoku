"""Tested functions

- set_cell
- clear_cell
"""

import unittest

from board import Board


class TestLogic(unittest.TestCase):

    def test_set_cell(self):
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
        board = Board(initial_state)

        # Case 1: Move is possible
        self.assertTrue(
            board.set_cell(3, 3, 5),
            "Should be a valid move because the cell is empty",
        )

        board.state[3][3] = 0
        board.zeroes += 1

        # Case 2: Cell is already filled
        self.assertFalse(
            board.set_cell(0, 0, 6),
            "Should not be a valid move because the cell is already filled",
        )

        # Case 3: Cell is empty, but the move is invalid
        self.assertFalse(
            board.set_cell(3, 3, 6),
            "Should not be a valid move",
        )

    def test_clear_cell(self):
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
        board = Board(initial_state)

        # Case 1: Clearing is possible
        self.assertTrue(
            board.clear_cell(0, 0),
            "Should be possible to clear a set cell",
        )
        self.assertTrue(
            board.zeroes == 3,
            "Should have 3 zeroes now",
        )

        board.state[0][0] = 1
        board.zeroes -= 1

        # Case 2: Cell is already empty
        self.assertFalse(
            board.clear_cell(3, 3),
            "Should not be a valid move because the cell is already empty",
        )
        self.assertTrue(
            board.zeroes == 2,
            "Should still have 2 zeroes",
        )


if __name__ == "__main__":
    unittest.main()
