from board import Board
from players import HumanPlayer, ComputerPlayer
from game import Game


def main():
    # one, both or none players can be the COMPUTER and choose colours automatically by random
    print("If you want play with computer, for player name put COMPUTER")
    player1_name = input("Put name of first player ")
    player2_name = input("Put name of second player ")

    # creating players
    if player1_name.upper() == "COMPUTER":
        codemaker = ComputerPlayer()
    else:
        codemaker = HumanPlayer(player1_name)
    if player2_name.upper() == "COMPUTER":
        codebreaker = ComputerPlayer()
    else:
        codebreaker = HumanPlayer(player2_name)

    # setting number of games wished to play
    while True:
        game_num = input("How many games you want to play? ")
        try:
            game_num = int(game_num)
            break
        except ValueError:
            print("You must put number!")

    for i in range(game_num):

        print(f"\nNow {codemaker.get_name()} is setting pattern and {codebreaker.get_name()} is guessing ")
        board = Board()  # new empty board
        game = Game(codemaker, codebreaker, board)  # two players playing game on board
        result = game.game()  # results can be "Win" or "Lost"
        board.print_pattern_board_hits(result)  # all played game is print on screen at once
        codemaker, codebreaker = codebreaker, codemaker  # players change the role

    print("\nTHIS IS THE END")
    print(f"{codebreaker.get_name()} won {codebreaker.get_result()[0]} times")
    print(f"{codemaker.get_name()} won {codemaker.get_result()[0]} times")


if __name__ == '__main__':
    main()
