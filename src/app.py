# type: ignore

"""The main application class, which handles the Kivy integration."""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window

from board import Board
from utils import EXAMPLE_BOARD
from utils import WINDOW_SIZE

Window.size = WINDOW_SIZE


class SudokuGrid(GridLayout):
    pass


class SudokuApp(App):
    def build(self):
        self.board = Board(EXAMPLE_BOARD)
        self.cells = [[Button() for _ in range(9)] for _ in range(9)]
        self.selected_grid: tuple[int, int] = (-1, -1)

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

    def on_cell_press(self, button: Button):
        row = int(button.pos_hint["row"])
        col = int(button.pos_hint["col"])

        self.selected_grid = (row, col)

        print(f"Selected ({row}, {col}).")

    def on_number_press(self, button: Button):
        if self.selected_grid != (-1, -1):
            row, col = self.selected_grid
            if not self.board.set_cell(row, col, int(button.text)):
                print("Invalid move.")
                return
            else:
                self.cells[row][col].text = button.text


if __name__ == "__main__":
    SudokuApp().run()
