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
        self.board: Board = Board(EXAMPLE_BOARD)
        self.cells: list[list[Button]] = [
            [Button() for _ in range(9)] for _ in range(9)
        ]

        sudoku_grid = self.root.ids.sudoku_grid
        for i in range(9):
            for j in range(9):
                number: int = self.board.state[i][j]
                num_text: str = str(number) if number != 0 else ""

                button: Button = self.cells[i][j]
                button.text: str = num_text
                button.pos_hint: dict[str, int] = {"row": i, "col": j}
                button.bind(on_press=self.on_cell_press)
                sudoku_grid.add_widget(button)

    def on_cell_press(self, button: Button) -> None:
        row: int = int(button.pos_hint["row"])
        col: int = int(button.pos_hint["col"])
        # if self.board.clear_cell(row, col):
        #     button.text = ""
        #     print(self.board)


if __name__ == "__main__":
    SudokuApp().run()
