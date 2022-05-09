from copy import deepcopy
from functools import cached_property

from src.board import Board, Outcome
from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy


class MinimaxDecision(MoveSelectionStrategy):
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player

    def perform(self, board):
        root = Node.fromBoard(board, self.player)

        v = self.max_value(root)
        return max(root.successors, key=lambda n: n._utility).action

    def max_value(self, state):
        if state.is_terminal_state():
            return state.utility(self.player)

        v = -float("inf")
        for s in state.successors:
            v = max(v, self.min_value(s))
        state._utility = v
        return state._utility

    def min_value(self, state):
        if state.is_terminal_state():
            return state.utility(self.player)

        v = float("inf")
        for s in state.successors:
            v = min(v, self.max_value(s))
        state._utility = v
        return state._utility


class Node:
    def __init__(self, board, piece, action=None):
        self.state = board
        self.player = piece
        self.action = action
        self._utility = None

    @cached_property
    def successors(self):
        if self.is_terminal_state():
            return []

        def successor(move):
            board = deepcopy(self.state)
            board.do_move(self.player, move)
            return Node(board, self.player.opposite, move)

        return [successor(coordinate) for coordinate in self.state.valid_moves()]

    def is_terminal_state(self):
        return self.state.is_game_over()

    def utility(self, player):
        if self._utility is not None:
            return self._utility

        outcome = self.state.check_for_game_over()
        if outcome is None:
            return None

        if outcome is Outcome.DRAW:
            self._utility = 0
        elif outcome is Outcome.fromPlayer(player):
            self._utility = 1
        else:
            self._utility = -1

        return self._utility

    @classmethod
    def fromBoard(cls, board, player):
        state = [
            [board[r, c] and board[r, c].piece() for c in range(3)] for r in range(3)
        ]
        return cls(Board(state), player)
