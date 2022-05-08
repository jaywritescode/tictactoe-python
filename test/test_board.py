from assertpy import assert_that
import pytest

from src.board import Outcome
from src.player import Piece


def test_getitem(after_five_plies, playerX, playerO):
    board = after_five_plies.board
    assert_that(board[1, 2]).is_same_as(Piece.O)
    assert_that(board[2, 2]).is_same_as(Piece.X)
    assert_that(board[0, 0]).is_none


def test_setitem_in_empty_square(after_five_plies, playerO):
    board = after_five_plies.board

    board[0, 0] = playerO
    assert_that(board[0, 0]).is_same_as(playerO)


def test_setitem_in_occupied_square(after_five_plies, playerO):
    board = after_five_plies.board

    with pytest.raises(ValueError):
        board[1, 1] = playerO


def test_do_move(after_five_plies):
    game = after_five_plies
    board = game.board
    player = game.players.peek()

    move = (0, 0)

    board.do_move(player, move)
    assert_that(board[move].piece()).is_same_as(player.piece())


def test_check_for_game_over_winner_x(win_for_x):
    assert_that(win_for_x.check_for_game_over()).is_same_as(Outcome.X)


# def test_check_for_game_over_winner_o(win_for_o):
#     pass


def test_check_for_game_over_outcome_draw(drawn_game):
    assert_that(drawn_game.check_for_game_over()).is_same_as(Outcome.DRAW)
