# type: ignore

"""The main application class, which handles the Kivy integration

The UI is made in the sudoku.kv file, so this file is just a wrapper.
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class SudokuGrid(GridLayout):
    pass


class SudokuApp(App):
    def on_start(self):
        sudoku_grid = self.root.ids.sudoku_grid
        for i in range(9):
            for j in range(9):
                cell = Button(text=f"{i},{j}")
                sudoku_grid.add_widget(cell)


if __name__ == "__main__":
    SudokuApp().run()
