from assertpy import assert_that
from unittest import mock
import pytest

from src.board import Board
from src.strategies.AskHuman import AskHuman


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
def test_valid(input_value, expected_index):
    with mock.patch("src.strategies.AskHuman.input", create=True) as mock_input:
        mock_input.return_value = input_value
        assert_that(AskHuman().perform(Board())).is_equal_to(expected_index)


def test_invalid_regexp():
    with mock.patch("src.strategies.AskHuman.input", create=True) as mock_input:
        mock_input.side_effect = ["abc", "1,2"]
        AskHuman().perform(Board())
        assert_that(mock_input.call_count).is_equal_to(2)


@pytest.mark.parametrize("input_value", ["0,1", "1,0", "4,1", "1,4"])
def test_out_of_bounds(input_value):
    with mock.patch("src.strategies.AskHuman.input", create=True) as mock_input:
        mock_input.side_effect = [input_value, "1,2"]
        AskHuman().perform(Board())
        assert_that(mock_input.call_count).is_equal_to(2)


def test_square_is_occupied(after_five_plies):
    board = after_five_plies.board
    with mock.patch("src.strategies.AskHuman.input", create=True) as mock_input:
        mock_input.side_effect = ["2,3", "3,1"]
        AskHuman().perform(board)
        assert_that(mock_input.call_count).is_equal_to(2)
