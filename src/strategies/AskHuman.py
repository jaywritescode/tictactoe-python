import re
from src.strategies.MoveSelectionStrategy import MoveSelectionStrategy


class AskHuman(MoveSelectionStrategy):
    def perform(self, board, player):
        while True:
            m = re.fullmatch(
                r"(?P<row>\d).+(?P<col>\d)", input("Play where? (upper-right is 1,3) ")
            )
            if not m:
                print("Invalid. Try again.")
                continue

            row, col = tuple([int(m[g]) - 1 for g in ["row", "col"]])
            if (not 0 <= row < 3) or (not 0 <= col < 3):
                print(
                    "Both coordinates must be greater than zero and less than or equal to three."
                )
                continue
            if board[row, col] is not None:
                print("That square is occupied.")
                continue

            return (row, col)
