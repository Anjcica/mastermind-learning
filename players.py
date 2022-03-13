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

    def set_win(self):
        self.__win += 1

    def set_lost(self):
        self.__lost += 1

    def get_name(self):
        return self.name

    def get_result(self):
        return [self.__win, self.__lost]
