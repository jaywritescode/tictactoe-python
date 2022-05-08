from itertools import cycle

from more_itertools import peekable

from src.board import Board
from src.player import Piece, Player


class TicTacToe:
    def __init__(self, strategy_x, strategy_o):
        self.board = Board()
        self.playerX = Player(Piece.X, strategy=strategy_x)
        self.playerO = Player(Piece.O, strategy=strategy_o)
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
