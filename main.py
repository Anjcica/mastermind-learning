from players import Player
from game import Game


def main():
    player1 = Player()
    player2 = Player()
    print("How many games you wont to play?")
    game_num = int(input())

    for i in range(game_num):
        print()
        print(f"Now {player1.get_name()} is setting pattern and {player2.get_name()} is guessing")
        game = Game(player1, player2)
        if game.game():
            player2.set_win()
        else:
            player2.set_lost()
        game.get_board()
        player1, player2 = player2, player1

    print("\nTHIS IS THE END")
    print(f"{player1.get_name()} won {player1.get_result()[0]} times")
    print(f"{player2.get_name()} won {player2.get_result()[0]} times")


if __name__ == '__main__':
    main()
