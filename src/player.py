from enum import Enum
import itertools
import random
import re

import minimax
from src.move import Move


Name = Enum("Name", ["X", "O"])


class AbstractPlayer:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def get_move(self):
        raise NotImplemented

    def __repr__(self):
        return self.name


class KeyboardInterfacePlayer(AbstractPlayer):
    def __init__(self, name, board):
        super().__init__(name, board)

    def get_move(self):
        print(self.board)

        while True:
            m = re.fullmatch(
                r"(?P<row>\d).+(?P<col>\d)", input("Play where? (upper-left is 1,1) ")
            )
            if not m:
                continue

            row, col = tuple([int(m[g]) - 1 for g in ["row", "col"]])
            if 0 <= row < 3 and 0 <= col < 3 and self.board[row, col] is None:
                return Move(self, (row, col))

            print("Invalid choice, try again.")





class MinimaxPlayer(AbstractPlayer):
    def __init__(self, name, game):
        super().__init__(name, game)

    def get_move(self):
        return minimax.minimax_decision(self.game)
