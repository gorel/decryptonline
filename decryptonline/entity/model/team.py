#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from decryptonline.entity.model.board import Board
from decryptonline.entity.model.player import Player
from decryptonline.entity.model.score_card import ScoreCard


@dataclass_json
@dataclass
class Team:
    name: str
    score_card: ScoreCard
    board: Board
    players: List[Player]
    intercept_tokens: int = 0
    miscommunication_tokens: int = 0
