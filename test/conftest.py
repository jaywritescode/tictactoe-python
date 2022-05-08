from more_itertools import consume
import pytest

from src.player import Piece, Player
from src.tictactoe import TicTacToe


@pytest.fixture
def playerX():
    return Player(Piece.X)


@pytest.fixture
def playerO():
    return Player(Piece.O)


@pytest.fixture
def initial_state():
    return TicTacToe()


@pytest.fixture
def after_one_ply():
    game = TicTacToe()
    game.board[2, 1] = Piece.X

    consume(game.players, 1)

    return game


@pytest.fixture
def after_five_plies():
    """
     | |O
    -+-+-
    X|X|O
    -+-+-
     | |X
    """
    game = TicTacToe()
    game.board[1, 1] = Piece.X
    game.board[0, 2] = Piece.O
    game.board[1, 0] = Piece.X
    game.board[1, 2] = Piece.O
    game.board[2, 2] = Piece.X

    consume(game.players, 5)

    return game


@pytest.fixture
def x_to_play_and_win():
    game = TicTacToe()
    game.board[1, 1] = Piece.X
    game.board[1, 2] = Piece.O
    game.board[0, 2] = Piece.X
    game.board[2, 0] = Piece.O
    game.board[0, 0] = Piece.X
    game.board[2, 1] = Piece.O

    consume(game.players, 6)

    return game


@pytest.fixture
def win_for_x(x_to_play_and_win):
    game = x_to_play_and_win
    game.board[0, 1] = Piece.X

    consume(game.players, 1)

    return game


@pytest.fixture
def drawn_game(after_five_plies):
    game = after_five_plies

    game.board[0, 0] = Piece.O
    game.board[2, 0] = Piece.X
    game.board[2, 1] = Piece.O
    game.board[0, 1] = Piece.X

    consume(game.players, 4)

    return game
