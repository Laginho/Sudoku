"""Terminal interface for playing the Sudoku game.

Provides a simple text-based loop that prompts the user for moves and updates
the board until the puzzle is solved.
"""

from board import Board
from utils import is_valid_input


def main():
    """The main loop for the terminal version of the game.

    On each move, the user gives an input of row, column, and value. Then,
    the move is validated, and the board is printed to the console.
    """

    board = Board()

    while not board.is_solved():
        print(board)
        while True:
            entry: list[str] = input("Row Column Value (1-9): ").split(" ")

            if not is_valid_input(entry):
                print("Invalid input.")
                continue

            row: int = int(entry[0]) - 1
            col: int = int(entry[1]) - 1
            val: int = int(entry[2])

            if not board.set_cell(row, col, val):
                print("Invalid move.")
                continue

            break

    print("You won!")


if __name__ == "__main__":
    main()
