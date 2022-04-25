from unittest.mock import MagicMock
from assertpy import assert_that

from src.move import Move


def test_x_can_play(initial_state):
    game = initial_state
    player = game.playerX

    player.get_move = MagicMock(
        name="get_move", return_value=Move(game.playerX, (1, 1))
    )

    game.next()
    assert_that(game.board).has_board(
        [[None, None, None], [None, player, None], [None, None, None]]
    )


def test_o_can_play(after_one_ply):
    game = after_one_ply
    playerX, playerO = game.playerX, game.playerO

    playerO.get_move = MagicMock(
        name="get_move", return_value=Move(game.playerO, (0, 0))
    )

    game.next()
    assert_that(game.board).has_board(
        [[playerO, None, None], [None, None, None], [None, playerX, None]]
    )
