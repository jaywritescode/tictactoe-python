from src.strategies.AskHuman import AskHuman
from src.strategies.MinimaxDecision import MinimaxDecision
from src.strategies.RandomMoves import RandomMoves


class StrategyFactory:
    def __init__(self, player):
        self.player = player

    def random(self):
        return RandomMoves()

    def human(self):
        return AskHuman()

    def minimax(self):
        return MinimaxDecision(self.player)

    def get(self, strategy):
        return getattr(self, strategy, self.random())()
