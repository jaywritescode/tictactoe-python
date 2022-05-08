import argparse
from src.tictactoe import TicTacToe


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tic-tac-toe w/ minimax decision algorithm")
    parser.add_argument("--strategy-x", default='random', choices=['human', 'random', 'minimax'], 
        help="how player X should select their move")
    parser.add_argument("--strategy-o", default='random', choices=['human', 'random', 'minimax'], 
        help="how player O should select their move")
    argv = parser.parse_args()

    tictactoe = TicTacToe(**vars(argv))
    tictactoe.play()
    tictactoe.print()
