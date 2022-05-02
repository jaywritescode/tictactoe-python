from unittest.mock import MagicMock
from assertpy import assert_that

from src.tictactoe import TicTacToe


def test_x_can_play():
    game = TicTacToe()

    player = game.playerX
    player.get_move = MagicMock(
        name="get_move", return_value=(1, 1)
    )

    game.next()
    assert_that(game.board).has_squares(
        [[None, None, None], [None, player, None], [None, None, None]]
    )


def test_o_can_play(after_one_ply):
    game = after_one_ply
    
    playerX, playerO = game.playerX, game.playerO
    playerO.get_move = MagicMock(
        name="get_move", return_value=(0, 0)
    )

    game.next()
    assert_that(game.board).has_squares(
        [[playerO, None, None], [None, None, None], [None, playerX, None]]
    )
