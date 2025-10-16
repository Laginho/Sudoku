# type: ignore

"""The main application class, which handles the Kivy integration."""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from copy import deepcopy as copy

from board import Board
from utils import EXAMPLE_BOARD, WINDOW_SIZE
from utils import Colors as c

Window.size = WINDOW_SIZE


class GameScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class SudokuGrid(GridLayout):
    pass


class WinPopup(Popup):
    pass


class SudokuApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(GameScreen(name="game"))
        return self.sm

    def game_start(self):
        self.board = Board(copy(EXAMPLE_BOARD))
        self.cells = [[Button() for _ in range(9)] for _ in range(9)]
        self.initial_cells = []
        self.selected_button: Button | None = None
        self.selected_grid: tuple[int, int] = (-1, -1)

        sudoku_grid = self.sm.get_screen("game").ids.sudoku_grid
        sudoku_grid.clear_widgets()
        for i in range(9):
            for j in range(9):
                number = self.board.state[i][j]
                button = self.cells[i][j]

                if number != 0:
                    self.initial_cells.append((i, j))
                    num_text = str(number)
                    button.background_color = c.GRAY
                else:
                    num_text = ""

                button.text = num_text
                button.pos_hint = {"row": i, "col": j}
                button.bind(on_press=self.on_cell_press)

                sudoku_grid.add_widget(button)

        number_palette = self.sm.get_screen("game").ids.number_palette
        number_palette.clear_widgets()
        for i in range(1, 10):
            number_button = Button(text=str(i))
            number_button.bind(on_press=self.on_number_press)
            number_palette.add_widget(number_button)
        clear_button = Button(text="Clear")
        clear_button.bind(on_press=self.on_number_press)
        number_palette.add_widget(clear_button)

    def on_cell_press(self, button: Button):
        row = int(button.pos_hint["row"])
        col = int(button.pos_hint["col"])

        if self.selected_button:
            self.selected_button.background_color = (
                c.GRAY if self.selected_button.text != "" else c.WHITE
            )

        if (row, col) in self.initial_cells:
            self.selected_grid = (-1, -1)
            self.selected_button = None
            return

        self.selected_grid = (row, col)
        self.selected_button = button
        button.background_color = c.SELECTED

    def on_number_press(self, button: Button):
        if self.selected_grid == (-1, -1) or not self.selected_button:
            return

        row, col = self.selected_grid
        number_to_set = int(button.text) if button.text != "Clear" else 0

        if number_to_set == 0:
            self.board.clear_cell(row, col)
            self.selected_button.text = ""
            self.selected_button.background_color = c.WHITE

        elif self.board.set_cell(row, col, number_to_set):
            self.selected_button.background_color = c.GRAY
            self.selected_button.text = str(number_to_set)
            if self.board.is_solved():
                self.show_win_popup()
        else:
            print("Invalid move.")
            return

        self.selected_grid = (-1, -1)
        self.selected_button = None

    def show_win_popup(self):
        """Finds the popup in the kv file and opens it."""

        pop = WinPopup()
        pop.open()

    def quit(self):
        """Goes back to the Main Menu."""

        self.sm.current = "menu"


if __name__ == "__main__":
    SudokuApp().run()
