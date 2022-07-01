from dataclasses import dataclass
from typing import List

from decryptonline.service.entity.model.board import Board
from decryptonline.service.entity.model.player import Player
from decryptonline.service.entity.model.score_card import ScoreCard


@dataclass
class Team:
    score_card: ScoreCard
    board: Board
    players: List[Player]
    intercept_tokens: int
    miscommunication_tokens: int
