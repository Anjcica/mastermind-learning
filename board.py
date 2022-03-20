from const import MastermindConst as const
import os


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

    for i in range(50):
        print()  # for IDLE


class Board:
    def __init__(self):
        self.__max_rows = const.MAX_ROWS
        self.__max_columns = const.MAX_COLUMNS
        self.__pattern = []
        self.__board = []
        self.__hits = []

    # class Game call this method to give pattern which codemaker create
    def set_pattern(self, new_row):
        self.__pattern = new_row
        screen_clear()

    # not in use in this version
    def get_pattern(self):
        return self.__pattern

    # class Game call this method to give colours which codebreaker choose
    def set_new_row(self, new_row):
        self.__board.append(new_row)

    # not in use in this version
    def get_last_row(self):
        return self.__board[-1]

    # class Game call this method to give number of guessed colours and position
    def set_hits(self, new_hits):
        self.__hits.append(new_hits)
        print(f"you hit {new_hits[0]} correct positions and colors and "
              f"{new_hits[1]} more correct colors in the wrong position")

    # not in use in this version
    def get_last_hits(self):
        return self.__hits[-1]

    # not in use in this version
    def get_all_board(self):
        return self.__board

    # call from main to show all played results
    def print_pattern_board_hits(self, result):
        screen_clear()
        if result == "Win":
            print("YOU WIN, CONGRATULATED!")
        elif result == "Lost":
            print("SORRY, YOU LOST")
        print("Pattern was :")
        print(self.__pattern)
        print("Fill board and hits are:")
        for i in range(len(self.__board)):
            print(self.__board[i], self.__hits[i])
