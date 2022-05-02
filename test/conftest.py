from more_itertools import consume
import pytest
from src.player import Name, Player
from src.players.keyboard_interface_player import KeyboardInterfacePlayer

from src.tictactoe import TicTacToe

@pytest.fixture
def playerX():
    return Player(Name.X)

@pytest.fixture
def playerO():
    return Player(Name.O)

@pytest.fixture
def initial_state():
    return TicTacToe()

@pytest.fixture
def after_one_ply():
    game = TicTacToe(playerO_class=KeyboardInterfacePlayer)
    game.board[2, 1] = game.playerX
    consume(game.players, 1)
    return game
