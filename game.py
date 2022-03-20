from const import MastermindConst as const


# class ones call codemaker.create_row and many times codebreaker_create row,
# all results are set in board by calling methods boar.set_pattern,
# board.set_new_board and board.set_hits
class Game:
    def __init__(self, codemaker, codebreaker, empty_board):
        self.board = empty_board
        self.codemaker = codemaker
        self.codebreaker = codebreaker
        self.codemaker_row = self.codemaker.create_row()
        self.board.set_pattern(self.codemaker_row)
        self.codebreaker_row = []
        self.full_rows = 0

    # calculate how many colours and position codebreaker guess
    def __guess_pattern(self):
        list_random_left_colours = []
        list_player_left_colours = []
        guessed_items = 0  # count right colours on right position
        for item in enumerate(self.codemaker_row):
            if item in enumerate(self.codebreaker_row):
                guessed_items += 1
            else:  # left lists of colours not on right position
                list_random_left_colours.append(item[1])
                list_player_left_colours.append(self.codebreaker_row[item[0]])

        guessed_colours = 0  # count how many right colours , but not on right position
        for colour in list((set(list_random_left_colours))):
            colour_random_left = list_random_left_colours.count(colour)
            colour_player_left = list_player_left_colours.count(colour)
            guessed_colours += (colour_player_left if colour_player_left < colour_random_left else colour_random_left)

        return guessed_items, guessed_colours

    # call codebreaker.create_row until is not game over
    def game(self):
        while True:
            self.codebreaker_row = self.codebreaker.create_row()
            self.board.set_new_row(self.codebreaker_row)
            self.full_rows += 1
            guessed_items, guessed_colours = self.__guess_pattern()
            self.board.set_hits((guessed_items, guessed_colours))
            if guessed_items == const.MAX_COLUMNS:
                self.codebreaker.set_win()
                return "Win"
            elif self.full_rows >= const.MAX_ROWS:
                self.codebreaker.set_lost()
                return "Lost"
