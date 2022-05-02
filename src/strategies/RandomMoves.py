import itertools
import random

from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy

class RandomMoves(MoveSelectionStrategy):
    def perform(self, board):
        empty_squares = [(row, col) for row, col in itertools.product(range(3), repeat=2) if board[row, col] is None]
        return random.choice(empty_squares)