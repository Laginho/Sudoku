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