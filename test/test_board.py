from assertpy import assert_that
import pytest
from src.board import Outcome
from src.move import Move

from src.player import Name


def test_getitem(after_five_plies, playerX, playerO):
    board = after_five_plies.board
    assert_that(board[1,2]).is_same_as(playerO)
    assert_that(board[2,2]).is_same_as(playerX)
    assert_that(board[0,0]).is_none

def test_setitem_in_empty_square(after_five_plies, playerO):
    board = after_five_plies.board

    board[0,0] = playerO
    assert_that(board[0,0]).is_same_as(playerO)

def test_setitem_in_occupied_square(after_five_plies, playerO):
    board = after_five_plies.board

    with pytest.raises(ValueError):
        board[1,1] = playerO

def test_do_move(after_five_plies, playerO):
    board = after_five_plies.board
    move = Move(player=playerO, coordinate=(0,0))

    board.do_move(move)
    assert_that(board[0,0]).is_same_as(playerO)

def test_check_for_game_over_winner_x(win_for_x):
    assert_that(win_for_x.check_for_game_over()).is_same_as(Outcome.X)

def test_check_for_game_over_winner_o(win_for_o):
    pass

def test_check_for_game_over_outcome_draw(drawn_game):
    assert_that(drawn_game.check_for_game_over()).is_same_as(Outcome.DRAW)
