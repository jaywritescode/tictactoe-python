from assertpy import assert_that
import pytest

from src.strategies.RandomMoves import RandomMoves

@pytest.mark.repeat(10)
def test_it_never_picks_an_occupied_square(after_five_plies):
    board = after_five_plies.board
    assert_that(RandomMoves().perform(board)).is_in((0,0), (0,1), (2,0), (2,1))