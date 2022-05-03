import random

from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy


class RandomMoves(MoveSelectionStrategy):
    def perform(self, board):
        return random.choice(board.valid_moves())
