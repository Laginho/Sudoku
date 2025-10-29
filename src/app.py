# pylint: disable=no-member, unused-import, attribute-defined-outside-init

"""Kivy application and UI components for the Sudoku game.

This module contains the main :class:`SudokuApp` application class and a few
lightweight widget subclasses that are referenced from ``sudoku.kv``.

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


from copy import deepcopy as copy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle

from board import Board
import constants as c
import settings as s
import db_utils


Window.size = s.WINDOW_SIZE
Window.clearcolor = c.DEFAULT


class GameScreen(Screen):
    """The main game screen."""


class MenuScreen(Screen):
    """The main menu screen."""


# class SudokuGrid(GridLayout):
#     """The Sudoku grid layout."""


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

        db_utils.setup_database()
        db_utils.add_puzzles()
        return self.sm

    def game_start(self):
        """Loads a new puzzle.

        The grid is populated with buttons corresponding to
        the puzzle state, marks initial cells as uneditable, and sets up the
        number palette.
        """

        # Database setup

        puzzle_grid = db_utils.load_puzzle_from_db()

        if not puzzle_grid:
            print("could not find a puzzle to load.")
            puzzle_grid = copy(c.EXAMPLE_BOARD)

        # Board setup

        self.board = Board(puzzle_grid)
        self.selected_grid: tuple[int, int] = (-1, -1)
        self.selected_button: Button | None = None
        self.cells: list[list[Button]] = [
            [Button() for _ in range(9)] for _ in range(9)
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
            number_button = Button(text=str(i), font_size=s.NUMBER_SIZE)
            number_button.background_normal = ""
            number_button.background_color = (
                0.9 * c.DEFAULT[0],
                0.9 * c.DEFAULT[1],
                0.9 * c.DEFAULT[2],
                1,
            )
            number_button.color = c.BLUE
            number_button.bind(on_press=self.on_number_press)
            number_palette.add_widget(number_button)

        clear_button = Button(text="C", font_size=s.NUMBER_SIZE)
        clear_button.color = c.BLUE
        clear_button.background_normal = ""
        clear_button.background_color = (
            0.9 * c.DEFAULT[0],
            0.9 * c.DEFAULT[1],
            0.9 * c.DEFAULT[2],
            1,
        )
        clear_button.bind(on_press=self.on_number_press)
        number_palette.add_widget(clear_button)

    def on_cell_press(self, button: Button):
        """Handles the pressing of a cell button on the Sudoku grid.

        Args:
            button: The Kivy button instance that was pressed.
        """

        row = int(button.pos_hint["row"])
        col = int(button.pos_hint["col"])

        if self.selected_button:
            self.selected_button.background_color = c.DEFAULT

        if (row, col) in self.board.initial_cells:
            self.selected_grid = (-1, -1)
            self.selected_button = None
            return

        self.selected_grid = (row, col)
        self.selected_button = button
        button.background_color = c.SELECTED

    def on_number_press(self, button: Button):
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

            pencil_set = self.board.pencil_marks[row][col]
            if number_to_set in pencil_set:
                pencil_set.remove(number_to_set)
            else:
                pencil_set.add(number_to_set)

            pencil_text = " ".join(map(str, sorted(list(pencil_set))))
            self.selected_button.text = pencil_text
            self.selected_button.font_size = s.NUMBER_SIZE // 3
            self.selected_button.color = c.BLUE

            self.selected_grid = (-1, -1)
            self.selected_button = None
            return

        self.selected_button.font_size = s.NUMBER_SIZE
        self.selected_button.color = c.BLACK
        if number_to_set == 0:
            self.board.clear_cell(row, col)
            self.selected_button.text = ""
            self.selected_button.background_color = c.DEFAULT

        elif self.board.set_cell(row, col, number_to_set):
            self.selected_button.background_color = c.DEFAULT
            self.selected_button.text = str(number_to_set)
            if self.board.is_solved():
                self.show_win_popup()
        else:
            print("Invalid move.")
            return

        self.selected_grid = (-1, -1)
        self.selected_button = None

    def toggle_pencil_mode(self):
        """Toggles pencil mode on or off."""

        self.pencil_mode = not self.pencil_mode
        self.update_pencil_button_visual()

    def update_pencil_button_visual(self):
        """Updates the pencil button's appearance based on the mode."""

        pencil_button = self.sm.get_screen("game").ids.pencil_button

        if self.pencil_mode:
            pencil_button.background_color = c.GREEN

            if self.selected_button:
                self.selected_grid = (-1, -1)
                self.selected_button.background_color = c.DEFAULT
                self.selected_button = None
            return

        pencil_button.background_color = c.LGRAY

    def show_win_popup(self):
        """Finds the popup in the kv file and opens it."""

        pop = WinPopup()
        pop.open()

    def quit(self):
        """Goes back to the Main Menu."""

        self.sm.current = "menu"


if __name__ == "__main__":
    SudokuApp().run()
