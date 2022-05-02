from enum import Enum

Name = Enum("Name", ["X", "O"])


class Player:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name.name

    def get_move(self):
        raise NotImplemented

    def __str__(self):
        return self.name
