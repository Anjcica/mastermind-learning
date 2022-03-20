from random import choice
from const import MastermindConst as const


class PlayerExceptions (Exception):
    pass


class Player:
    max_players = 0

    def __init__(self, name):
        Player.max_players += 1
        if Player.max_players <= 2:
            self.name = name
            self.__win = 0
            self.__lost = 0
        else:
            raise PlayerExceptions("Too much players")

    # class Game increases victories
    def set_win(self):
        self.__win += 1

    # class Game increases losses
    def set_lost(self):
        self.__lost += 1

    def get_name(self):
        return self.name

    def get_result(self):
        return [self.__win, self.__lost]


# creating row choosing colors by random
class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self, name="Computer")

    def create_row(self):  # for simulate computer
        new_row = []
        for i in range(const.MAX_COLUMNS):
            new_row.append(choice(const.COLOURS))
        return new_row


# creating row that human chooses colours
class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.name = name

    def create_row(self):
        print(f"{self.name} please choose {const.MAX_COLUMNS} colors between {const.COLOURS}")
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
