class Board:
    def __init__(self):
        self.board = [[None for col in range(3)] for row in range(3)]
    
    def __getitem__(self, coordinate):
        (row, col) = coordinate
        return self.board[row][col]

    def __setitem__(self, coordinate, value):
        (row, col) = coordinate
        self.board[row][col] = value