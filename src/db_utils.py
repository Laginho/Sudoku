"""Functions for working with the SQLite database."""

import sqlite3

from utils import parse_puzzle_string

DB_NAME: str = "sudoku_puzzles.db"


def setup_database(db_name: str = DB_NAME) -> None:
    """Creates the table in the database if it doesn't already exist.

    It's kind of overkill for this game, but it is more of an excuse for
    learning SQLite and its practical implementations.

    Args:
        db_name: The name of the database file. Defaults to DB_NAME.

    Raises:
        sqlite3.Error: If a database operation fails during the table creation.
    """

    sql = """
        CREATE TABLE IF NOT EXISTS puzzles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            puzzle_string TEXT NOT NULL UNIQUE,
            difficulty TEXT
        );
        """
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    except sqlite3.Error as e:
        print(f"Database error during setup: {e}")


def add_puzzles(db_name: str = DB_NAME) -> None:
    """Adds a predefined list of Sudoku puzzles to the database

    Honorable mention to INSERT OR IGNORE, meaning puzzles that already exist
    will not be re-inserted.

    Args:
        db_name (str): The name of the database file. Defaults to DB_NAME.

    Raises:
        sqlite3.Error: If a database operation fails during the insertion process.
    """

    puzzles: list[tuple[str, str]] = [
        (
            "050703060007000800000816000"
            "000030000005000100730040086"
            "906000204840572093000409000",
            "easy",
        ),
        (
            "302401809001000300000000000"
            "040708010780502036000090000"
            "200609003900000008800070005",
            "easy",
        ),
        (
            "020900000048000031000063020"
            "009407003003080200400105600"
            "030570000250000180000006050",
            "medium",
        ),
        (
            "100800570000009210090040000"
            "300900050007000300020006008"
            "000020040071400000064007003",
            "medium",
        ),
    ]

    sql: str = """
        INSERT OR IGNORE INTO puzzles (puzzle_string, difficulty) 
        VALUES (?, ?); 
        """

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()

            for puzzle_str, difficulty in puzzles:
                cursor.execute(sql, (puzzle_str, difficulty))

    except sqlite3.Error as e:
        print(f"Database error adding puzzles: {e}")


def load_puzzle_from_db(
    difficulty: str = "easy", db_name: str = DB_NAME
) -> list[list[int]]:
    """Loads a random puzzle from the database with the specified difficulty.

    Args:
        difficulty (str): The difficulty level to filter by
                          (e.g., 'easy', 'medium'). Defaults to 'easy'.

        db_name (str): The name of the database file. Defaults to DB_NAME.

    Returns:
        A 9x9 list of lists representing the puzzle or an empty 2d list
        if no valid puzzle is found for the difficulty.

    Raises:
        sqlite3.Error: If a database operation fails during the query process.
    """

    sql: str = """
        SELECT puzzle_string FROM puzzles 
        WHERE difficulty = ? ORDER BY RANDOM() LIMIT 1
        """
    puzzle_grid = [[]]

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (difficulty,))
            result = cursor.fetchone()

            if result:
                puzzle_str = result[0]
                puzzle_grid: list[list[int]] = parse_puzzle_string(puzzle_str)

    except sqlite3.Error as e:
        print(f"Database error loading puzzle: {e}")

    if not puzzle_grid:
        print(f"No valid puzzle found for difficulty: {difficulty}")

    return puzzle_grid
