from assertpy import assert_that
import pytest
from src.board import Board
from src.player import Piece

from src.strategies.MinimaxDecision import Node


@pytest.fixture
def after_five_plies_node(after_five_plies):
    board = after_five_plies.board
    return Node.fromBoard(board, after_five_plies.playerO)


def test_successors_root_node(after_five_plies_node):
    node = after_five_plies_node
    successors = node.successors()
    assert_that(successors).is_length(4)
    assert_that(successors).extracting('player').contains_only(Piece.X)
    assert_that(successors).extracting('state', filter=lambda s: s.state.matches(Board([
        [Piece.O, None, Piece.O], [Piece.X, Piece.X, Piece.O], [None, None, Piece.X]
    ]))).is_not_empty()
    assert_that(successors).extracting('state', filter=lambda s: s.state.matches(Board([
        [None, Piece.O, Piece.O], [Piece.X, Piece.X, Piece.O], [None, None, Piece.X]
    ]))).is_not_empty()
    assert_that(successors).extracting('state', filter=lambda s: s.state.matches(Board([
        [None, None, Piece.O], [Piece.X, Piece.X, Piece.O], [Piece.O, None, Piece.X]
    ]))).is_not_empty()
    assert_that(successors).extracting('state', filter=lambda s: s.state.matches(Board([
        [None, None, Piece.O], [Piece.X, Piece.X, Piece.O], [None, Piece.O, Piece.X]
    ]))).is_not_empty()


def test_is_not_terminal_state(after_five_plies_node):
    node = after_five_plies_node
    assert_that(node.is_terminal_state()).is_false


def test_is_terminal_state_with_win(win_for_x):
    board = win_for_x.board
    node = Node(board, win_for_x.playerO)
    assert_that(node.is_terminal_state()).is_true


def test_is_terminal_state_with_draw(drawn_game):
    board = drawn_game.board
    node = Node(board, drawn_game.playerO)
    assert_that(node.is_terminal_state()).is_true()


def test_utility_with_game_in_progress(after_five_plies):
    game = after_five_plies
    node = Node(game.board, game.playerO)
    assert_that(node.utility(game.playerO)).is_none


def test_utility_with_draw(drawn_game):
    pass


def test_utility_with_win():
    pass


def test_utility_with_loss():
    pass
