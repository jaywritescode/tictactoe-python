from unittest import mock
from assertpy import assert_that
import pytest

from src.players.keyboard_interface_player import KeyboardInterfacePlayer
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
    with mock.patch(
        "src.players.keyboard_interface_player.input", create=True
    ) as mock_input:
        tictactoe = TicTacToe(playerX_class=KeyboardInterfacePlayer)
        mock_input.return_value = input_value

        move = tictactoe.playerX.get_move()
        assert_that(move).has_player(tictactoe.playerX).has_selection(expected_index)


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
        # ("3,2", (2, 1)),  already played
        ("3,3", (2, 2)),
    ],
)
def test_player_two_get_move(after_one_ply, input_value, expected_index):
    with mock.patch(
        "src.players.keyboard_interface_player.input", create=True
    ) as mock_input:
        tictactoe = after_one_ply
        mock_input.return_value = input_value

        move = tictactoe.playerO.get_move()
        assert_that(move).has_player(tictactoe.playerO).has_selection(expected_index)


def test_cannot_play_at_occupied_coordinate(after_one_ply):
    with mock.patch(
        "src.players.keyboard_interface_player.input", create=True
    ) as mock_input:
        tictactoe = after_one_ply
        mock_input.side_effect = ["3,2", "1,1"]

        move = tictactoe.playerO.get_move()
        assert_that(mock_input.call_count).is_equal_to(2)
        assert_that(move).has_selection((0, 0))
