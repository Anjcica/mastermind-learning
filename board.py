from const import MastermindConst as const

# board for playing define like list of lists
class Board:
    def __init__(self):
        self.__max_rows = const.MAX_ROWS
        self.__max_columns = const.MAX_COLUMNS
        self.__pattern = []
        self.__board = []
        self.__hits = []

    def set_pattern(self, new_row):
        self.__pattern = new_row

    def set_new_row(self, new_row):
        self.__board.append(new_row)

    def set_hits(self, new_hits):
        self.__hits.append(new_hits)

    def board_full(self):
        return len(self.__board) >= self.__max_rows

    def get_board(self):
        return self.__board

    def get_pattern(self):
        return self.__pattern

    def get_hits(self):
        return self.__hits
