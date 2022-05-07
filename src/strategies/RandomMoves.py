import random

from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy


class RandomMoves(MoveSelectionStrategy):
    def perform(self, board, player):
        return random.choice(board.valid_moves())
