from enum import Enum

from src.strategies.RandomMoves import RandomMoves

Name = Enum("Name", ["X", "O"])


class Player:
    def __init__(self, name, strategy=RandomMoves()):
        self._name = name
        self.strategy = strategy

    @property
    def name(self):
        return self._name.name

    def get_move(self, board):
        return self.strategy.perform(board)

    def __str__(self):
        return self.name
