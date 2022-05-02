from itertools import cycle

from src.board import Board
from src.player import Name, Player
from src.players.keyboard_interface_player import KeyboardInterfacePlayer


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.playerX = Player(Name.X)
        self.playerO = Player(Name.O)

        self.players = cycle([self.playerX, self.playerO])
        self.outcome = None

    def play(self):
        while self.outcome is None:
            self.next()

    def next(self):
        current_player = next(self.players)
        self.board.do_move(current_player.get_move())
        self.outcome = self.check_for_game_over()

    def check_for_game_over(self):
        return self.board.check_for_game_over()
