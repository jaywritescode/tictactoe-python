from dataclasses import dataclass
from minimax import State

from src.player import Name


@dataclass(frozen=True)
class BoardState:
    rows: tuple[tuple[Name]]

    def __getitem__(self, coordinate):
        (row, col) = coordinate
        return self.rows[row][col]

    def successor(self, player_name, row, col):
        succ = tuple(
            tuple(player_name if (r, c) == (row, col) else self[r, c] for c in range(3))
            for r in range(3)
        )
        return BoardState(succ)


@dataclass(frozen=True)
class MinimaxState(State):
    ply: int
    name: str
    next_player: Name
    board: BoardState

    def __init__(self, ply, name, next_player, board):
        self.ply = ply
        self.name = name
        self.next_player = next_player

        board_tuple = tuple(
            tuple(board[row][col] for col in range(3)) for row in range(3)
        )
        self.board = BoardState(board_tuple)

    def successors(self):
        def successor(row, col):
            next_ply = self.ply + 1
            return MinimaxState(
                ply=next_ply,
                name=f"{next_ply}. ({row},{col})",
                next_player=Name.X if self.next_player is Name.O else Name.O,
                board=self.board.successor(self.next_player, row, col),
            )

        return [
            successor(row, col)
            for row in range(3)
            for col in range(3)
            if self.board[row, col] is None
        ]
