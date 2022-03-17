from players import HumanPlayer, ComputerPlayer
from game import Game


def main():
    # both, one or none players can be the COMPUTER
    print("If you want play with computer, for player name put COMPUTER")
    player1_name = input("Put name of first player ")
    player2_name = input("Put name of second player ")

    if player1_name.upper() == "COMPUTER":
        codemaker = ComputerPlayer()
    else:
        codemaker = HumanPlayer(player1_name)

    if player2_name.upper() == "COMPUTER":
        codebreaker = ComputerPlayer()
    else:
        codebreaker = HumanPlayer(player2_name)

    while True:
        game_num = input("How many games you want to play? ")
        try:
            game_num = int(game_num)
            break
        except ValueError:
            print("You must put number!")

    for i in range(game_num):
        print()
        print(f"Now {codemaker.get_name()} is setting pattern and {codebreaker.get_name()} is guessing ")

        game = Game(codemaker, codebreaker)
        if game.game():
            codebreaker.set_win()
        else:
            codebreaker.set_lost()
        game.print_board()
        codemaker, codebreaker = codebreaker, codemaker

    print("\nTHIS IS THE END")
    print(f"{codemaker.get_name()} won {codemaker.get_result()[0]} times")
    print(f"{codebreaker.get_name()} won {codebreaker.get_result()[0]} times")


if __name__ == '__main__':
    main()
