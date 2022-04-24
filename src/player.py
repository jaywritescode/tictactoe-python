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







class MinimaxPlayer(AbstractPlayer):
    def __init__(self, name, game):
        super().__init__(name, game)

    def get_move(self):
        return minimax.minimax_decision(self.game)
