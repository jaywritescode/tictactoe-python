from enum import Enum

Name = Enum("Name", ["X", "O"])


class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def get_move(self):
        raise NotImplemented

    def __repr__(self):
        return self.name
