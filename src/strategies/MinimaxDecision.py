from dataclasses import dataclass


def perform(self, board):
    root = Node(board)


@dataclass
class Action:
    move: tuple[int, int]


class Node:
    def __init__(self, board):
        self.state = board

    def successors(self):
        pass

    def is_terminal_state(self):
        pass

    def utility(self):
        pass
