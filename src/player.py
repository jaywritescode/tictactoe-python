from enum import Enum

Name = Enum("Name", ["X", "O"])


class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self):
        raise NotImplemented

    def __str__(self):
        return self.name.name
