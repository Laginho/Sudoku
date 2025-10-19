# pylint: disable=C0115
# pylint: disable=C0111
"""Tested functions

- setup_database
- add_puzzles
- load_puzzle_from_db
"""

import unittest
import sqlite3

from db_utils import (
    setup_database,
    add_puzzles,
    load_puzzle_from_db,
)


class TestDbUtils(unittest.TestCase):

    test_db_name: str = "test_puzzles.db"

    def setUp(self) -> None:
        setup_database(db_name=self.test_db_name)

    def tearDown(self) -> None:
        pass

    def test_setup_database(self) -> None:
        with sqlite3.connect(self.test_db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='puzzles';"
            )
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], "puzzles")

    def test_add_puzzles(self) -> None:
        with self.subTest(msg="Should add the correct number of puzzles to a new DB"):
            add_puzzles(db_name=self.test_db_name)
            with sqlite3.connect(self.test_db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM puzzles;")
                count = cursor.fetchone()[0]
                self.assertEqual(count, 4)

        with self.subTest(msg="Should not add duplicate puzzles (idempotency)"):
            add_puzzles(db_name=self.test_db_name)
            with sqlite3.connect(self.test_db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM puzzles;")
                count = cursor.fetchone()[0]
                self.assertEqual(count, 4)

    def test_load_puzzle_from_db(self) -> None:
        add_puzzles(db_name=self.test_db_name)

        with self.subTest(msg="Should return a valid 'easy' puzzle grid"):
            puzzle = load_puzzle_from_db(difficulty="easy", db_name=self.test_db_name)
            self.assertEqual(len(puzzle), 9)
            self.assertEqual(len(puzzle[0]), 9)
            self.assertIsInstance(puzzle[0][0], int)

        with self.subTest(msg="Should return a valid 'medium' puzzle grid"):
            puzzle = load_puzzle_from_db(difficulty="medium", db_name=self.test_db_name)
            self.assertEqual(len(puzzle), 9)
            self.assertEqual(len(puzzle[0]), 9)
            self.assertIsInstance(puzzle[0][0], int)

        with self.subTest(
            msg="Should return an empty grid for a non-existent difficulty"
        ):
            puzzle = load_puzzle_from_db(
                difficulty="impossible", db_name=self.test_db_name
            )
            self.assertEqual(puzzle, [[]])

        with self.subTest(msg="Should return an empty grid from an empty database"):
            with sqlite3.connect(self.test_db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM puzzles;")
                conn.commit()
            puzzle = load_puzzle_from_db(difficulty="easy", db_name=self.test_db_name)
            self.assertEqual(puzzle, [[]])


if __name__ == "__main__":
    unittest.main()
