from more_itertools import consume
import pytest

from src.player import Name, Player
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
def after_one_ply(playerX):
    game = TicTacToe()
    game.playerX = playerX

    game.board[2, 1] = playerX

    consume(game.players, 1)

    return game


@pytest.fixture
def after_five_plies(playerX, playerO):
    """
     | |O
    -+-+-
    X|X|O
    -+-+-
     | |X
    """
    game = TicTacToe()
    game.playerX = playerX
    game.playerO = playerO

    game.board[1, 1] = playerX
    game.board[0, 2] = playerO
    game.board[1, 0] = playerX
    game.board[1, 2] = playerO
    game.board[2, 2] = playerX

    consume(game.players, 5)

    return game


@pytest.fixture
def x_to_play_and_win(playerX, playerO):
    game = TicTacToe()
    game.playerX = playerX
    game.playerO = playerO

    game.board[1, 1] = playerX
    game.board[1, 2] = playerO
    game.board[0, 2] = playerX
    game.board[2, 0] = playerO
    game.board[0, 0] = playerX
    game.board[2, 1] = playerO

    consume(game.players, 6)

    return game


@pytest.fixture
def win_for_x(x_to_play_and_win):
    game = x_to_play_and_win

    game.board[0, 1] = game.playerX

    consume(game.players, 1)

    return game


@pytest.fixture
def drawn_game(after_five_plies):
    game = after_five_plies

    game.board[0, 0] = game.playerO
    game.board[2, 0] = game.playerX
    game.board[2, 1] = game.playerO
    game.board[0, 1] = game.playerX

    consume(game.players, 4)

    return game
