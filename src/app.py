# pylint: disable=no-member, unused-import, attribute-defined-outside-init, protected-access

"""Kivy application and UI components for the Sudoku game.

This module contains the main :class:`SudokuApp` application class and a few
lightweight widget subclasses that are referenced from ``layout.kv``.

The application is responsible for loading puzzles from the database,
instantiating the :class:`Board`, wiring UI callbacks and showing the win
popup when the puzzle is solved.

Classes:
    SudokuApp: Kivy :class:`~kivy.app.App` subclass that manages the game UI.
    GameScreen: Screen used for the game view.
    MenuScreen: Screen used for the main menu.
    SudokuGrid: GridLayout used to display the 9x9 board.
    WinPopup: Popup shown when the player solves the puzzle.
"""

import os
import sys
from copy import deepcopy as copy

from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, RoundedRectangle

from board import Board
import logic
import constants as c
import settings as s
import db_utils

# Path handling for Windows & PyInstaller

# if hasattr(sys, "_MEIPASS"):
#     resource_add_path(os.path.join(sys._MEIPASS))
#     KV_FILE_PATH = os.path.join(sys._MEIPASS, "layout.kv")
#     DB_PATH = os.path.join(sys._MEIPASS, "data/sudoku_puzzles.db")
#     TXT_PATH = os.path.join(sys._MEIPASS, "data/puzzles.txt")
# else:
#     project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     resource_add_path(project_root)
#     KV_FILE_PATH = "src/layout.kv"
#     DB_PATH = "data/sudoku_puzzles.db"
#     TXT_PATH = "data/puzzles.txt"

# project_root = os.path.dirname(os.path.abspath(__file__))
# resource_add_path(os.path.join(project_root, "assets"))
# Builder.load_file(KV_FILE_PATH)

# Path handling for Android & Buildozer

Builder.load_file("layout.kv")
DB_PATH = db_utils.get_db_path()
TXT_PATH = db_utils.get_txt_path()

# Kivy Window setup

Window.size = s.WINDOW_SIZE
Window.clearcolor = c.DEFAULT


class GameScreen(Screen):
    """The main game screen."""


class MenuScreen(Screen):
    """The main menu screen."""


# class SudokuGrid(GridLayout):
#     """The Sudoku grid layout."""


class NumberButton(Button):
    """Button used for numbers in the palette."""


class WinPopup(Popup):
    """Popup displayed when the player wins."""


class SudokuApp(App):
    """The main application.

    This class manages the overall flow and UI of the Sudoku game,
    including screen transitions, puzzle loading, board setup, user
    input handling and game completion feedback.

    Attributes:
        sm (ScreenManager):
            Manages different screens in the application.

        board (Board):
            Represents the current game board object and its state.

        selected_grid (tuple[int, int]):
            Coordinates of the currently selected cell.

        selected_button (Button | None):
            Reference to the currently selected button in the grid.

        cells (list[list[Button]]):
            2D list of buttons representing the Sudoku grid.
    """

    def build(self):
        """Initializes the application.

        The database is set up and puzzles are added.

        Returns:
            ScreenManager: The root widget of the application.
        """

        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(GameScreen(name="game"))
        self.pencil_mode = False
        self.difficulty = "Not selected"

        # db_utils.setup_database(db_name=DB_PATH)
        # db_utils.add_puzzles_from_file(TXT_PATH, db_name=DB_PATH)
        return self.sm

    def game_start(self, difficulty: str):
        """Loads a new puzzle.

        The grid is populated with buttons corresponding to
        the puzzle state, marks initial cells as uneditable, and sets up the
        number palette.
        """

        # Database setup

        print(f"Loading a {difficulty} puzzle...")
        self.difficulty = difficulty
        puzzle_grid = db_utils.load_puzzle_from_db(self.difficulty, db_name=DB_PATH)
        # puzzle_grid = copy(c.EXAMPLE_BOARD)  # Debugging
        self.sm.get_screen("game").ids.difficulty_label.text = (
            self.difficulty.capitalize()
        )

        if not puzzle_grid or puzzle_grid == [[]] or puzzle_grid == [[0] * 9] * 9:
            print("could not find a puzzle to load.")
            puzzle_grid = copy(c.EXAMPLE_BOARD)

        # Board setup

        self.board = Board(puzzle_grid)
        self.selected_grid: tuple[int, int] = (-1, -1)
        self.selected_button: NumberButton | None = None
        self.cells: list[list[NumberButton]] = [
            [NumberButton() for _ in range(9)] for _ in range(9)
        ]
        self.pencil_mode = False
        self.update_pencil_button_visual()

        # Board UI setup

        sudoku_grid = self.sm.get_screen("game").ids.sudoku_grid
        sudoku_grid.clear_widgets()
        for i in range(9):
            for j in range(9):
                number = self.board.state[i][j]
                button = self.cells[i][j]

                if number != 0:
                    self.board.initial_cells.add((i, j))
                    num_text = str(number)
                else:
                    num_text = ""

                button.pos_hint = {"row": i, "col": j}
                button.bind(on_press=self.on_cell_press)

                button.text = num_text
                button.font_size = s.NUMBER_SIZE
                button.background_normal = ""
                button.background_color = c.DEFAULT
                button.color = c.BLACK

                sudoku_grid.add_widget(button)

        # Number palette UI setup

        number_palette = self.sm.get_screen("game").ids.number_palette
        number_palette.clear_widgets()
        for i in range(1, 10):
            number_button = NumberButton(text=str(i), font_size=s.NUMBER_SIZE)
            number_button.bind(on_press=self.on_number_press)
            number_palette.add_widget(number_button)
            number_button.size_hint = (1, 1)

        clear_button = NumberButton(text="C", font_size=s.NUMBER_SIZE)
        clear_button.bind(on_press=self.on_number_press)
        number_palette.add_widget(clear_button)
        clear_button.size_hint = (1, 1)

    def on_cell_press(self, button: NumberButton):
        """Handles the pressing of a cell button on the Sudoku grid.

        Args:
            button: The Kivy button instance that was pressed.
        """

        row = int(button.pos_hint["row"])
        col = int(button.pos_hint["col"])

        if self.selected_button:
            self.selected_button.background_color = c.DEFAULT

        if (row, col) in self.board.initial_cells:
            self.deselect_button()
            return

        self.selected_grid = (row, col)
        self.selected_button = button
        button.background_color = c.SELECTED

    def on_number_press(self, button: NumberButton):
        """Handles the pressing of a number button in the palette.

        Args:
            button: The Kivy button instance that was pressed.
        """

        if self.selected_grid == (-1, -1) or not self.selected_button:
            return

        row, col = self.selected_grid
        number_to_set = int(button.text) if button.text != "C" else 0

        if self.pencil_mode:
            if number_to_set == 0:
                return

            if not logic.check_move(self.board.state, row, col, number_to_set):
                return

            pencil_set = self.board.pencil_marks[row][col]
            if number_to_set in pencil_set:
                pencil_set.remove(number_to_set)
            else:
                pencil_set.add(number_to_set)

            self.update_pencil_marks()
            return

        if number_to_set == 0:
            self.board.clear_cell(row, col)
            self.selected_button.text = ""
            self.selected_button.background_color = c.DEFAULT
            self.board.pencil_marks[row][col].clear()

        elif self.board.set_cell(row, col, number_to_set):
            self.selected_button.background_color = c.DEFAULT
            self.selected_button.color = c.BLACK
            self.selected_button.font_size = s.NUMBER_SIZE
            self.selected_button.text = str(number_to_set)

            self.board.pencil_marks[row][col].clear()
            self.update_all_marks()

            if self.board.is_solved():
                self.show_win_popup()
        else:
            print("Invalid move.")
            print(self.board)
            return

        self.deselect_button()

    def toggle_pencil_mode(self):
        """Toggles pencil mode on or off."""

        self.pencil_mode = not self.pencil_mode
        self.update_pencil_button_visual()

    def update_pencil_marks(self):
        """Updates the display of pencil marks on the selected grid.

        The text is rendered as a 3x3 grid, with each number having
        its reserved spot.
        """

        row, col = self.selected_grid
        pencil_set = self.board.pencil_marks[row][col]

        text_lines = ["", "", ""]
        for num in range(1, 10):
            line_idx = (num - 1) // 3
            pos_in_line = (num - 1) % 3
            if num in pencil_set:
                text_lines[line_idx] += str(num)
            else:
                text_lines[line_idx] += "   "
            if pos_in_line < 2:
                text_lines[line_idx] += "   "

        self.cells[row][col].font_size = s.NUMBER_SIZE // 3
        self.cells[row][col].color = c.DGRAY
        self.cells[row][col].text = "\n".join(text_lines)

    def update_all_marks(self):
        """Updates pencil marks for all cells on the board."""

        for i in range(9):
            for j in range(9):
                if (i, j) in self.board.initial_cells:
                    continue
                if self.board.state[i][j] != 0:
                    continue

                self.selected_grid = (i, j)
                self.selected_button = self.cells[i][j]

                self.update_pencil_marks()

        self.deselect_button()

    def update_pencil_button_visual(self):
        """Updates the pencil button's appearance based on the mode."""

        pencil_button = self.sm.get_screen("game").ids.pencil_button

        pencil_button.canvas.before.clear()
        if self.pencil_mode:
            with pencil_button.canvas.before:
                Color(*c.SELECTED)
                bg = RoundedRectangle(
                    pos=pencil_button.pos,
                    size=pencil_button.size,
                    radius=[(12, 12)] * 4,
                )
        else:
            with pencil_button.canvas.before:
                Color(0, 0, 0, 0)
                bg = RoundedRectangle(
                    pos=pencil_button.pos,
                    size=pencil_button.size,
                    radius=[(12, 12)] * 4,
                )

        def _update_bg(instance, _):
            bg.pos = instance.pos
            bg.size = instance.size

        pencil_button.bind(pos=_update_bg, size=_update_bg)

        pencil_button.background_color = (0, 0, 0, 0)

    def auto_pencil(self):
        """Automatically fills in all possible pencil marks."""

        for i in range(9):
            for j in range(9):
                if (i, j) in self.board.initial_cells:
                    continue
                if self.board.state[i][j] != 0:
                    continue

                self.selected_grid = (i, j)
                self.selected_button = self.cells[i][j]

                pencil_set = set()
                for num in range(1, 10):
                    if logic.check_move(self.board.state, i, j, num):
                        pencil_set.add(num)

                self.board.pencil_marks[i][j] = pencil_set
                self.update_pencil_marks()
                self.deselect_button()

    def deselect_button(self):
        """Deselects the currently selected button, if any."""

        if self.selected_button:
            self.selected_button.background_color = c.DEFAULT
            self.selected_button = None
            self.selected_grid = (-1, -1)

    def reset(self):
        """Resets the current puzzle to its initial state."""

        for i in range(9):
            for j in range(9):
                if (i, j) in self.board.initial_cells:
                    continue

                self.board.clear_cell(i, j)
                self.cells[i][j].text = ""
                self.cells[i][j].color = c.BLACK
                self.cells[i][j].font_size = s.NUMBER_SIZE
                self.board.pencil_marks[i][j].clear()

        self.deselect_button()

    def show_win_popup(self):
        """Finds the popup in the kv file and opens it."""

        pop = WinPopup()
        pop.open()

    def quit(self):
        """Goes back to the Main Menu."""

        self.sm.current = "menu"


if __name__ == "__main__":
    SudokuApp().run()
