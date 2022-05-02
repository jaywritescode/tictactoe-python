from dataclasses import dataclass

from src.player import Player


@dataclass(frozen=True)
class Move:
    player: Player
    coordinate: tuple[int, int]
