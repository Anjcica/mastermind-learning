from const import Const as c
from const import MyExceptions as e


class Board:
    def __init__(self):
        self.max_rows = c.MAX_ROWS
        self.max_columns = c.MAX_COLUMNS
        self.__board = []

    def set_new_row(self, new_row):
        if len(self.__board) <= c.MAX_ROWS + 1 and len(new_row) == c.MAX_COLUMNS:  # row 0 is for code pattern
            self.__board.append(new_row)
        else:
            raise e("No more space on board or row ")

    def print_board(self):
        print("Pattern was :")
        print(self.__board[0])
        print("Fill board was:")
        for i in range(1, len(self.__board)):
            print(self.__board[i])
