from enum import Enum, auto

from src.strategies.RandomMoves import RandomMoves

class Name(Enum):
    X = auto()
    O = auto()

    @property
    def opposite(self):
        return Name.O if self is Name.X else Name.X 

class Player:
    def __init__(self, name, strategy=RandomMoves()):
        self.name = name
        self.strategy = strategy

    def get_move(self, board):
        return self.strategy.perform(board)

    def __str__(self):
        return self.name.name
