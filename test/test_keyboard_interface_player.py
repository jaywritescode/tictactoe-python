from unittest import mock
from assertpy import assert_that
import pytest
from src.players import KeyboardInterfacePlayer

from src.tictactoe import TicTacToe


@pytest.mark.parametrize(
    "input_value, expected_index",
    [
        ("1,1", (0, 0)),
        ("1,2", (0, 1)),
        ("1 3", (0, 2)),
        ("2,1", (1, 0)),
        ("2,2", (1, 1)),
        ("2,3", (1, 2)),
        ("3,1", (2, 0)),
        ("3,2", (2, 1)),
        ("3,3", (2, 2)),
    ],
)
def test_player_one_get_move(input_value, expected_index):
    with mock.patch("src.players.input", create=True) as mock_input:
        tictactoe = TicTacToe(playerX_class=KeyboardInterfacePlayer)
        mock_input.return_value = input_value

        move = tictactoe.playerX.get_move()
        assert_that(move).has_player(tictactoe.playerX).has_selection(expected_index)
