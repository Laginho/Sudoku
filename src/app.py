# type: ignore

"""The main application class, which handles the Kivy integration

The UI is made in the sudoku.kv file, so this file is just a wrapper.
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from board import Board
from utils import EXAMPLE_BOARD


class SudokuGrid(GridLayout):
    pass


class SudokuApp(App):
    def build(self):

        self.board = Board(EXAMPLE_BOARD)

        sudoku_grid = self.root.ids.sudoku_grid
        for i in range(9):
            for j in range(9):
                number = self.board.state[i][j]
                num_text = str(number) if number != 0 else ""
                cell = Button(text=num_text)
                sudoku_grid.add_widget(cell)


if __name__ == "__main__":
    SudokuApp().run()
