import sqlite3


def execute_command(
    command: str,
    arg1: str | None = None,
    arg2: str | None = None,
    db_name: str = "sudoku_puzzles.db",
) -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(command, (arg1, arg2))

    conn.commit()
    conn.close()


def setup_database(db_name: str = "sudoku_puzzles.db") -> None:
    execute_command(
        """
        CREATE TABLE IF NOT EXISTS puzzles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            puzzle_string TEXT NOT NULL UNIQUE, 
            difficulty TEXT
        );
        """
    )


def add_puzzles(db_name: str = "sudoku_puzzles.db") -> None:
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

    for puzzle_str, difficulty in puzzles:
        execute_command(sql, puzzle_str, difficulty)
