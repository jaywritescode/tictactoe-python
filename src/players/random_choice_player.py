import itertools
import random

from src.move import Move
from src.player import Player


class RandomChoicePlayer(Player):
    def __init__(self, name, game):
        super().__init__(name, game)

    def get_move(self):
        empty_squares = [
            (row, col)
            for row, col in itertools.product([0, 1, 2], repeat=2)
            if self.board[row, col] is None
        ]
        return Move(self, random.choice(empty_squares))
