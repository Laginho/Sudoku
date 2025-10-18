# 📝 Sudoku

A Sudoku game. Shocking, i know.

***

## 🧩 Project Overview

**Sudoku** is a game application built using Python and the **Kivy** framework for the graphical user interface (GUI). It also includes a command-line interface (CLI) for terminal play.

The project is version **0.4** and is released under the **MIT License**.

***

## ⚙️ Dependencies

The project relies on standard Python libraries and the **Kivy** framework.

| Dependency | Purpose |
| :--- | :--- |
| **Kivy** | Used for building the cross-platform graphical user interface (`kivy.app.App`, `kivy.uix.screenmanager.ScreenManager`, etc.). |
| **sqlite3** | Python's standard library module for SQLite database interaction, used for storing puzzles (`db_utils.py`). |

***

## 🚀 Getting Started

### Running the Game

1.  **GUI Version (Kivy App):**
    The main Kivy application is started by running `src/app.py`. This file initializes the screen manager, sets up the database, adds predefined puzzles, and launches the menu screen.

2.  **Terminal Version (CLI):**
    The terminal interface is run via `src/terminal_game.py`, which prompts the user for "Row Column Value (1-9)" inputs until the board is solved.

***

## 📁 File Structure

| File/Directory | Description |
| :--- | :--- |
| `src/app.py` | The main Kivy application (`SudokuApp`) handling GUI, game state (selection, moves), screen navigation, and database initialization. |
| `src/sudoku.kv` | Kivy language file defining the UI components, screens (`MenuScreen`, `GameScreen`), and layout (`SudokuGrid`, `WinPopup`). |
| `src/board.py` | Defines the `Board` class for managing the 9x9 Sudoku state, including tracking empty cells (`zeroes`) and fixed initial cells. |
| `src/logic.py` | Contains the core validation functions (`check_row`, `check_col`, `check_sqr`, `check_board`) for Sudoku rules. |
| `src/db_utils.py` | Utility module for SQLite database operations, including creating the `puzzles` table, adding initial puzzles, and loading a random puzzle by difficulty. |
| `src/utils.py` | General utilities: constants like `WINDOW_SIZE`, `Colors`, `EXAMPLE_BOARD`, and helper functions like `has_nonzero_duplicate` and `count_zeroes`. |
| `test/` | Contains unit tests for `logic.py`, `utils.py`, and `board.py`. |

***

## 💻 Core Modules Details

### `src/board.py`

#### `class Board`
Manages the Sudoku board's state and interactions.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `state` | `list[list[int]]` | The current 9x9 board configuration (0 for empty). |
| `zeroes` | `int` | The number of empty cells on the board. |
| `initial_cells` | `set[tuple[int, int]]` | Coordinates of pre-filled cells that cannot be modified by the user. |

| Method | Description |
| :--- | :--- |
| `is_solved()` | Checks if the board is valid (`logic.check_board`) and completely filled (`self.zeroes == 0`). |
| `is_valid()` | Checks if the current state is valid according to Sudoku rules. |
| `set_cell(row, col, value)` | Sets a cell, but only if it's not an initial cell, currently empty, and results in a valid board state. |
| `clear_cell(row, col)` | Clears a cell (sets to 0), but only if it's not an initial cell and is currently filled. |

### `src/logic.py`

This module provides functions for validating Sudoku configurations.

| Function | Description |
| :--- | :--- |
| `check_row(state, row)` | Returns `True` if `state[row]` has no non-zero duplicates. |
| `check_col(state, col)` | Returns `True` if the specified column has no non-zero duplicates. |
| `check_sqr(state, sqr)` | Returns `True` if the specified 3x3 square (numbered 0-8 like a numpad) has no non-zero duplicates. |
| `check_board(state)` | Checks validity of all 9 rows, 9 columns, and 9 squares. |

### `src/db_utils.py`

This module manages the **`sudoku_puzzles.db`** SQLite database.

| Function | Description |
| :--- | :--- |
| `setup_database()` | Creates the `puzzles` table if it does not exist. The table columns are `id`, `puzzle_string` (TEXT, unique), and `difficulty` (TEXT). |
| `add_puzzles()` | Inserts a predefined list of "easy" and "medium" 81-character puzzle strings into the database using `INSERT OR IGNORE`. |
| `parse_puzzle_string(puzzle_str)` | Converts an 81-character string into a 9x9 list of lists of integers. |
| `load_puzzle_from_db(difficulty)` | Selects a random puzzle string of the given `difficulty` from the DB and returns it as a 9x9 grid. |

### `src/utils.py`

| Function/Class | Description |
| :--- | :--- |
| `WINDOW_SIZE` | Constant for the Kivy window size: `(405, 720)`. |
| `Colors` | Dataclass holding RGBA color tuples for the GUI (e.g., `WHITE`, `GRAY`, `SELECTED`). |
| `has_nonzero_duplicate(vector)` | Checks if a 1D list contains duplicates of any non-zero value. |
| `count_zeroes(state)` | Calculates the total number of `0`s (empty cells) in the 9x9 board state. |