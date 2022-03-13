import board
from const import MastermindConst as const
from random import choice
import os


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    for i in range(50):
        print()  # for IDLE


class Game:
    def __init__(self, codemaker, codebreaker):
        self.board = board.Board()
        self.codemaker = codemaker
        self.codebreaker = codebreaker

    @staticmethod
    def set_random_pattern():  # for simulate computer
        new_row = []
        for i in range(const.MAX_COLUMNS):
            new_row.append(choice(const.COLOURS))
        return new_row

    @staticmethod
    def set_row(name):  # for any player
        print(f"{name} please chose {const.MAX_COLUMNS} colors between {const.COLOURS}")
        num = 0
        new_row = []
        while num != const.MAX_COLUMNS:
            colour = input().upper()
            if colour in const.COLOURS:
                new_row.append(colour)
                num += 1
            else:
                print("Wrong colour, try again ")
        return new_row

    @staticmethod
    def __guess_pattern(codebreaker_row, codemaker_row):
        list_random_left_colours = []
        list_player_left_colours = []
        guessed_items = 0  # count same colour and position
        for item in enumerate(codemaker_row):
            if item in enumerate(codebreaker_row):
                guessed_items += 1
            else:  # left lists of colours not on right position
                list_random_left_colours.append(item[1])
                list_player_left_colours.append(codebreaker_row[item[0]])

        guessed_colours = 0  # count how many right colours , but not on right position
        for colour in list((set(list_random_left_colours))):
            colour_random_left = list_random_left_colours.count(colour)
            colour_player_left = list_player_left_colours.count(colour)
            guessed_colours += (colour_player_left if colour_player_left < colour_random_left else colour_random_left)

        return guessed_items, guessed_colours

    def game(self):
        if self.codemaker.get_name().upper() == "COMPUTER":
            codemaker_row = Game.set_random_pattern()
        else:
            codemaker_row = Game.set_row(self.codemaker.get_name())
        screen_clear()
        self.board.set_pattern(codemaker_row)
        while True:
            if self.codebreaker.get_name().upper() == "COMPUTER":
                codebreaker_row = Game.set_random_pattern()
            else:
                codebreaker_row = Game.set_row(self.codemaker.get_name())
            print(codebreaker_row)
            self.board.set_new_row(codebreaker_row)
            guessed_items, guessed_colours = Game.__guess_pattern(codebreaker_row, codemaker_row)
            if guessed_items == const.MAX_COLUMNS:
                print("\n\nYOU GUESS ALL CORRECT, CONGRATULATED!")
                return True
            elif self.board.board_full():
                print("GAME OVER, TRY AGAIN")
                return False
            else:
                print(f"you hit {guessed_items} correct positions and colors and "
                      f"{guessed_colours} more correct colors in the wrong position")

    def print_board(self):
        print("Pattern was :")
        print(self.board.get_pattern())
        print("Fill board was:")
        played_rows = self.board.get_board()
        for i in range(len(played_rows)):
            print(played_rows[i])
