class Move:
    def __init__(self, player, selection):
        self.player = player
        self.selection = selection

    def apply(self, board):
        board[self.selection] = self.player