from assertpy import assert_that

from src.strategies.MinimaxDecision import Node

def test_successors_root_node(after_five_plies):
    board = after_five_plies.board
    root = Node(board, after_five_plies.playerO)
    successors = root.successors()
    assert_that(successors).is_length(4)


def test_is_not_terminal_state(after_five_plies):
    board = after_five_plies.board
    node = Node(board)
    assert_that(node.is_terminal_state()).is_false

def test_is_terminal_state_with_win(win_for_x):
    board = win_for_x.board
    node = Node(board)
    assert_that(node.is_terminal_state()).is_true

def test_is_terminal_state_with_draw(drawn_game):
    board = drawn_game.board
    node = Node(board)
    assert_that(node.is_terminal_state()).is_true()