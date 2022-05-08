import argparse
from src.tictactoe import TicTacToe


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tic-tac-toe w/ minimax decision algorithm")
    parser.add_argument("--strategy-x", default='random', choices=['human', 'random', 'minimax'], 
        help="how player X should select their move")
    argv = parser.parse_args()

    print(argv)

    tictactoe = TicTacToe(strategy_x=argv.strategy_x)
    tictactoe.play()
    tictactoe.print()
