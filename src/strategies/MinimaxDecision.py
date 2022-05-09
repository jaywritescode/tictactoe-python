from copy import deepcopy

from src.board import Board, Outcome
from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy


class MinimaxDecision(MoveSelectionStrategy):
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player

    def perform(self, board):
        root = Node.fromBoard(self, board, self.player)

        v = self.max_value(root)

    def max_value(self, state):
        if state.is_terminal_state():
            return state.utility(self.player)

        v = -float("inf")
        for s in state.successors():
            v = max(v, self.min_value(s))
        return v

    def min_value(self, state):
        if state.is_terminal_state():
            return state.utility(self.player)

        v = float("inf")
        for s in state.successors():
            v = min(v, self.max_value(s))
        return v


class Node:
    def __init__(self, board, piece):
        self.state = board
        self.player = piece

    def successors(self):
        if self.is_terminal_state():
            return []

        def successor(move):
            board = deepcopy(self.state)
            board.do_move(self.player, move)
            return Node(board, self.player.opposite)

        return [successor(coordinate) for coordinate in self.state.valid_moves()]

    def is_terminal_state(self):
        return self.state.is_game_over()

    def utility(self, player):
        outcome = self.state.check_for_game_over()

        if outcome is None:
            return None
        if outcome is Outcome.DRAW:
            return 0
        if outcome is Outcome.fromPlayer(player):
            return 1
        else:
            return -1

    @classmethod
    def fromBoard(cls, board, player):
        state = [[board[r, c] and board[r, c].piece() for c in range(3)] for r in range(3)]
        return cls(Board(state), player)
