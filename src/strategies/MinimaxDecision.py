from copy import deepcopy

from src.board import Board
from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy

class MinimaxDecision(MoveSelectionStrategy):
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player

    def perform(self, board, player):
        root = Node(self, board, player)


class Node:
    def __init__(self, board, player):
        self.state = board
        self.player = player.name

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

    def utility(self):
        raise NotImplemented("is terminal node")
