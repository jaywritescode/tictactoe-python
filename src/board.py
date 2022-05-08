from enum import Enum, auto
import itertools

from more_itertools import all_equal, flatten


class Outcome(Enum):
    X = auto()
    O = auto()
    DRAW = auto()

    @classmethod
    def fromPlayer(cls, player):
        return cls.fromPlayerName(player.name)

    @classmethod
    def fromPlayerName(cls, name):
        return cls(name.value)


class Board:
    ROWS = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
    ]
    COLUMNS = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    ]
    DIAGONALS = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    def __init__(self, squares=None):
        if squares is None:
            self.squares = [[None for col in range(3)] for row in range(3)]
        else:
            self.squares = squares

    def __getitem__(self, coordinate):
        (row, col) = coordinate
        return self.squares[row][col]

    def __setitem__(self, coordinate, value):
        (row, col) = coordinate
        if self.squares[row][col] is not None:
            raise ValueError
        self.squares[row][col] = value

    def valid_moves(self):
        return [
            (row, col)
            for row, col in itertools.product(range(3), repeat=2)
            if not self[row, col]
        ]

    def do_move(self, player, move):
        self[move] = player.piece()

    def check_for_game_over(self):
        lines = Board.ROWS + Board.COLUMNS + Board.DIAGONALS
        for line in lines:
            line_squares = [self[coords] for coords in line]
            if all(square is not None for square in line_squares) and all_equal(
                value.piece() for value in line_squares
            ):
                player = line_squares[0].piece()
                return Outcome.fromPlayerName(player)

        if all(square is not None for square in flatten(self.squares)):
            return Outcome.DRAW

    def is_game_over(self):
        return self.check_for_game_over() is not None

    def __str__(self):
        row = "{}|{}|{}\n"
        sep = "-+-+-\n"

        return sep.join([row] * 3).format(
            *[
                getattr(self[row, col], "name", " ")
                for row in range(3)
                for col in range(3)
            ]
        )
