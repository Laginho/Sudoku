import sqlite3

DB_NAME: str = "sudoku_puzzles.db"


def setup_database(db_name: str = DB_NAME) -> None:
    """Creates the puzzles table if it doesn't exist."""

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
    """Adds a predefined list of puzzles to the database, ignoring duplicates."""

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


def parse_puzzle_string(puzzle_str: str) -> list[list[int]] | None:
    """Converts an 81-character string into a 9x9 grid."""

    if len(puzzle_str) != 81 or not puzzle_str.isdigit():
        return None

    grid: list[list[int]] = []

    try:
        for i in range(9):
            row_str = puzzle_str[i * 9 : (i + 1) * 9]
            row = [int(char) for char in row_str]
            grid.append(row)

        return grid

    except ValueError:
        return None


def load_puzzle_from_db(
    difficulty: str = "easy", db_name: str = DB_NAME
) -> list[list[int]] | None:
    """Loads a random puzzle string of a given difficulty and parses it."""

    sql: str = """
        SELECT puzzle_string FROM puzzles 
        WHERE difficulty = ? ORDER BY RANDOM() LIMIT 1
        """
    puzzle_grid = None

    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (difficulty,))
            result = cursor.fetchone()

            if result:
                puzzle_str = result[0]
                puzzle_grid = parse_puzzle_string(puzzle_str)

    except sqlite3.Error as e:
        print(f"Database error loading puzzle: {e}")

    if not puzzle_grid:
        print(f"No valid puzzle found for difficulty: {difficulty}")

    return puzzle_grid
