from players import Player
from game import Game


def main():
    print("If you want play with computer, for player name put COMPUTER")  # both players can be the COMPUTER
    player1 = Player(input("Put name of first player "))
    player2 = Player(input("Put name of second player "))
    game_num = int(input("How many games you want to play? "))

    for i in range(game_num):
        print()
        print(f"Now {player1.get_name()} is setting pattern and {player2.get_name()} is guessing ")
        game = Game(player1, player2)
        if game.game():
            player2.set_win()
        else:
            player2.set_lost()
        game.print_board()
        player1, player2 = player2, player1

    print("\nTHIS IS THE END")
    print(f"{player1.get_name()} won {player1.get_result()[0]} times")
    print(f"{player2.get_name()} won {player2.get_result()[0]} times")


if __name__ == '__main__':
    main()
