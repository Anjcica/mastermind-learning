from const import Const as c
import board


class Game:
    def __init__(self, codemaker, codebreaker):
        self.full_rows = 0
        self.board = board.Board()
        self.codemaker = codemaker
        self.codebreaker = codebreaker
        self.codemaker_row = self.codemaker.set_pattern()
        self.board.set_new_row(self.codemaker_row)
        self.full_rows = 0

    def __guess_pattern(self, codebreaker_row):
        list_random_left_colours = []
        list_player_left_colours = []
        guessed_items = 0  # count same colour and position
        for item in enumerate(self.codemaker_row):
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
        while True:
            codebreaker_row = self.codebreaker.set_pattern()
            self.full_rows += 1
            print(codebreaker_row)
            self.board.set_new_row(codebreaker_row)
            guessed_items, guessed_colours = self.__guess_pattern(codebreaker_row)
            if guessed_items == c.MAX_COLUMNS:
                print("YOU ALL GUESS CORRECT, CONGRATULATED!")
                return True
            elif self.full_rows == c.MAX_ROWS+1:  # row 0 is for code pattern
                print("GAME OVER, TRY AGAIN")
                return False
            else:
                print(f"You guess {guessed_items} places and colours + {guessed_colours} colours more")

    def get_board(self):
        self.board.print_board()
