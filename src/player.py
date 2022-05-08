from enum import Enum, auto

from src.strategies.RandomMoves import RandomMoves


class PlayerId:
    def piece(self):
        raise NotImplemented

    @property
    def opposite(self):
        return Piece.O if self.piece() is Piece.X else Piece.X


class Piece(PlayerId, Enum):
    X = auto()
    O = auto()

    def piece(self):
        return self


class Player(PlayerId):
    def __init__(self, name, strategy=RandomMoves()):
        self.name = name
        self.strategy = strategy

    def get_move(self, board):
        return self.strategy.perform(board)

    def piece(self):
        return self.name.piece()

    def __str__(self):
        return self.name.name
