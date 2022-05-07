from assertpy import assert_that
import pytest

from src.strategies.MinimaxDecision import Node


@pytest.fixture
def after_five_plies_node(after_five_plies):
    board = after_five_plies.board
    return Node(board, after_five_plies.playerO)


def test_successors_root_node(after_five_plies_node):
    node = after_five_plies_node
    successors = node.successors()
    assert_that(successors).is_length(4)


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
