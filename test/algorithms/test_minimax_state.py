from assertpy import assert_that

from src.algorithms import minimax
from src.board import Board
from src.move import Move
from src.player import Name

def test_successors_from_initial_board():
    board = Board()
    root = minimax.Node(board=board)

    expected = root.successors
    print(expected)




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
