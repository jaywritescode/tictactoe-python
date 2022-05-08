import argparse
from src.tictactoe import TicTacToe


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tic-tac-toe w/ minimax decision algorithm")
    argv = parser.parse_args()

    tictactoe = TicTacToe()
    tictactoe.play()
    tictactoe.print()
