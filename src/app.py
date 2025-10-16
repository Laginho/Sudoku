# type: ignore

"""The main application class, which handles the Kivy integration."""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

from board import Board
from utils import EXAMPLE_BOARD
from utils import WINDOW_SIZE

Window.size = WINDOW_SIZE


class SudokuGrid(GridLayout):
    pass


class WinPopup(BoxLayout):
    pass


class SudokuApp(App):
    def build(self):
        self.board = Board(EXAMPLE_BOARD)
        self.cells = [[Button() for _ in range(9)] for _ in range(9)]
        self.selected_grid: tuple[int, int] = (-1, -1)
        self.selected_button: Button | None = None

    def on_start(self):
        sudoku_grid = self.root.ids.sudoku_grid
        for i in range(9):
            for j in range(9):
                number = self.board.state[i][j]
                num_text = str(number) if number != 0 else ""

                button = self.cells[i][j]
                button.text = num_text
                button.pos_hint = {"row": i, "col": j}
                button.bind(on_press=self.on_cell_press)
                sudoku_grid.add_widget(button)

        number_palette = self.root.ids.number_palette
        for i in range(1, 10):
            number_button = Button(text=str(i))
            number_button.bind(on_press=self.on_number_press)
            number_palette.add_widget(number_button)

        self.show_win()

    def on_cell_press(self, button: Button):
        row = int(button.pos_hint["row"])
        col = int(button.pos_hint["col"])

        self.selected_grid = (row, col)

        if isinstance(self.selected_button, Button):
            self.selected_button.background_color = (1, 1, 1, 1)

        self.selected_button = button
        button.background_color = (0.5, 0.5, 1, 1)

        print(f"Selected ({row}, {col}).")

    def on_number_press(self, button: Button):
        if self.selected_grid != (-1, -1):
            row, col = self.selected_grid
            if not self.board.set_cell(row, col, int(button.text)):
                print("Invalid move.")
            else:
                print(f"Set ({row}, {col}) to {button.text}.")
                self.cells[row][col].text = button.text

            self.selected_button.background_color = (1, 1, 1, 1)
            self.selected_button = None

            if self.board.is_solved():
                self.show_win()

    def show_win(self):
        """Shows a popup message saying that the player has won."""
        popup = Popup(title="", content=WinPopup(), size_hint=(0.5, 0.5))
        popup.open()


if __name__ == "__main__":
    SudokuApp().run()
