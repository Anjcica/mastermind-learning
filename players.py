from const import Const as c
from const import MyExceptions as e
from random import choice


class Player:
    max_players = 0

    def __init__(self):
        Player.max_players += 1
        if Player.max_players <= 2:
            self.name = input(f"Put {Player.max_players}. players name ").upper()
            self.win = 0
            self.lost = 0
            self.__chosen_pattern = []
        else:
            raise e("Too much players")

    def set_pattern(self):
        print(f"{self.name} please chose {c.MAX_COLUMNS} colors between {c.COLOURS}")
        num = 0
        self.__chosen_pattern.clear()
        while num != c.MAX_COLUMNS:
            colour = input().upper()
            if colour in c.COLOURS:
                self.__chosen_pattern.append(colour)
                num += 1
            else:
                print("Wrong colour, try again ")
        return self.__chosen_pattern

    def random_pattern(self):
        self.__chosen_pattern.clear()
        for i in range(c.MAX_COLUMNS):
            self.__chosen_pattern.append(choice(c.COLOURS))
        return self.__chosen_pattern

    def set_win(self):
        self.win += 1

    def set_lost(self):
        self.lost += 1

    def get_name(self):
        return self.name

    def get_result(self):
        return [self.win, self.lost]
