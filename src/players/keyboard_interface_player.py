import re

from src.move import Move
from src.player import Player


class KeyboardInterfacePlayer(Player):
    def __init__(self, name, board):
        super().__init__(name, board)

    def get_move(self):
        print(self.board)

        while True:
            m = re.fullmatch(
                r"(?P<row>\d).+(?P<col>\d)", input("Play where? (upper-left is 1,1) ")
            )
            if not m:
                continue

            row, col = tuple([int(m[g]) - 1 for g in ["row", "col"]])
            if 0 <= row < 3 and 0 <= col < 3 and self.board[row, col] is None:
                return Move(self, (row, col))

            print("Invalid choice, try again.")
