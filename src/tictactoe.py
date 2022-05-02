from itertools import cycle

from more_itertools import peekable

from src.board import Board
from src.player import Name, Player


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.playerX = Player(Name.X)
        self.playerO = Player(Name.O)
        self.ply = 1

        self.players = peekable(cycle([self.playerX, self.playerO]))
        self.outcome = None

    def play(self):
        while self.outcome is None:
            self.print()
            self.next()

    def next(self):
        current_player = next(self.players)
        move = current_player.get_move(self.board)

        self.board.do_move(current_player, move)
        self.outcome = self.check_for_game_over()
        if not self.outcome:
            self.ply += 1

    def check_for_game_over(self):
        return self.board.check_for_game_over()

    def print(self):
        print("Ply #{}: {} to play".format(self.ply, self.players.peek().name))
        print(self.board)
