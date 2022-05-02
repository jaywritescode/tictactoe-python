from enum import Enum

from more_itertools import all_equal, flatten


Outcome = Enum("Outcome", ["X", "O", "DRAW"])


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

    def do_move(self, move):
        self[move.coordinate] = move.player

    def check_for_game_over(self):
        lines = Board.ROWS + Board.COLUMNS + Board.DIAGONALS
        for line in lines:
            line_squares = [self[coords] for coords in line]
            if all(square is not None for square in line_squares) and all_equal(
                line_squares
            ):
                player = line_squares[0]
                return Outcome[player.name]

        if all(square is not None for square in flatten(self.squares)):
            return Outcome.DRAW

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
