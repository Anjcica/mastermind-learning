from const import MastermindConst as const


class BoardExceptions (Exception):
    pass


class Board:
    def __init__(self):
        self.__max_rows = const.MAX_ROWS
        self.__max_columns = const.MAX_COLUMNS
        self.__pattern = []
        self.__board = []

    def set_pattern(self, new_row):
        self.__pattern = new_row

    def set_new_row(self, new_row):
        self.__board.append(new_row)

    def board_full(self):
        if len(self.__board) <= self.__max_rows:
            return False
        else:
            return True

    def get_board(self):
        return self.__board

    def get_pattern(self):
        return self.__pattern
