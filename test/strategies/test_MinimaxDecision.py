from assertpy import assert_that
from more_itertools import consume
import pytest

from src.board import Board
from src.player import Piece
from src.strategies.MinimaxDecision import Node
from src.tictactoe import TicTacToe


@pytest.fixture
def after_five_plies_node(after_five_plies):
    board = after_five_plies.board
    return Node.fromBoard(board, after_five_plies.playerO)


@pytest.fixture
def blunder_by_o():
    game = TicTacToe(strategy_x="minimax")
    game.board[1, 1] = Piece.X
    game.board[1, 0] = Piece.O
    game.board[0, 1] = Piece.X
    game.board[2, 1] = Piece.O

    consume(game.players, 2)

    return game


@pytest.fixture
def o_to_play_and_win():
    game = TicTacToe(strategy_o="minimax")
    game.board[1, 0] = Piece.X
    game.board[1, 1] = Piece.O
    game.board[0, 0] = Piece.X
    game.board[2, 0] = Piece.O
    game.board[2, 1] = Piece.X

    consume(game.players, 5)

    return game


def test_perform(o_to_play_and_win):
    game = o_to_play_and_win
    strategy = game.playerO.strategy

    assert_that(strategy.perform(game.board)).is_equal_to((0, 2))


def test_perform_deeper_search(blunder_by_o):
    game = blunder_by_o
    strategy = game.playerX.strategy

    assert_that(strategy.perform(game.board)).is_in((0, 0), (0, 2))


def test_successors_root_node(after_five_plies_node):
    node = after_five_plies_node
    successors = node.successors
    assert_that(successors).is_length(4)
    assert_that(successors).extracting("player").contains_only(Piece.X)
    assert_that(successors).extracting(
        "state",
        filter=lambda s: s.state.matches(
            Board(
                [
                    [Piece.O, None, Piece.O],
                    [Piece.X, Piece.X, Piece.O],
                    [None, None, Piece.X],
                ]
            )
        ),
    ).is_not_empty()
    assert_that(successors).extracting(
        "state",
        filter=lambda s: s.state.matches(
            Board(
                [
                    [None, Piece.O, Piece.O],
                    [Piece.X, Piece.X, Piece.O],
                    [None, None, Piece.X],
                ]
            )
        ),
    ).is_not_empty()
    assert_that(successors).extracting(
        "state",
        filter=lambda s: s.state.matches(
            Board(
                [
                    [None, None, Piece.O],
                    [Piece.X, Piece.X, Piece.O],
                    [Piece.O, None, Piece.X],
                ]
            )
        ),
    ).is_not_empty()
    assert_that(successors).extracting(
        "state",
        filter=lambda s: s.state.matches(
            Board(
                [
                    [None, None, Piece.O],
                    [Piece.X, Piece.X, Piece.O],
                    [None, Piece.O, Piece.X],
                ]
            )
        ),
    ).is_not_empty()


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
    game = drawn_game
    node = Node(game.board, game.playerO)
    assert_that(node.utility(game.playerX)).is_zero()


def test_utility_with_win(win_for_x):
    game = win_for_x
    node = Node(game.board, game.playerO)
    assert_that(node.utility(game.playerX)).is_equal_to(1)


def test_utility_with_loss(win_for_x):
    game = win_for_x
    node = Node(game.board, game.playerO)
    assert_that(node.utility(game.playerO)).is_equal_to(-1)
