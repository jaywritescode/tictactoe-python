from assertpy import assert_that

from src.algorithms.minimax_state import BoardState, MinimaxState
from src.player import Name

def test_board_state_successor():
    board = ((None, None, Name.O), (None, Name.X, None), (None, None, None))
    state = BoardState(board)

    successor = state.successor(Name.X, 2, 2)
    assert_that(successor).is_not_same_as(state)
    assert_that(successor.rows).is_equal_to(((None, None, Name.O), (None, Name.X, None), (None, None, Name.X)))





# def test_initial_state():
#     state = MinimaxState(ply=0, name='', next_player=Name.X, board=[[None for _ in range(3)] for _ in range(3)])

#     expected = [
#         ((Name.X, None, None), (None, None, None), (None, None, None)),
#         ((None, Name.X, None), (None, None, None), (None, None, None)),
#         ((None, None, Name.X), (None, None, None), (None, None, None)),
#         ((None, None, None), (Name.X, None, None), (None, None, None)),
#         ((None, None, None), (None, Name.X, None), (None, None, None)),
#         ((None, None, None), (None, None, Name.X), (None, None, None)),
#         ((None, None, None), (None, None, None), (Name.X, None, None)),
#         ((None, None, None), (None, None, None), (None, Name.X, None)),
#         ((None, None, None), (None, None, None), (None, None, Name.X)),
#     ]
#     assert_that(state.successors()).contains_only(expected)
#     assert_that(state.terminal_test()).is_false()