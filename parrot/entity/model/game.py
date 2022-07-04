#!/usr/bin/env python3

from dataclasses import dataclass, field
from enum import Enum, auto

from dataclasses_json import dataclass_json

from parrot.entity.model.score_card import ScoreCard
from parrot.entity.model.team import Team


@dataclass_json
@dataclass
class GameStatus(Enum):
    TEAM1_PLAY = auto()
    TEAM2_PLAY = auto()
    TEAM1_WON = auto()
    TEAM2_WON = auto()
    DRAW = auto()


DEFAULT_WIN_THRESHOLD = 2


@dataclass_json
@dataclass
class Game:
    status: GameStatus
    team1: Team
    team2: Team
    score_card: ScoreCard = field(default_factory=ScoreCard)
    round: int = 1
    interception_win_threshold: int = DEFAULT_WIN_THRESHOLD
    miscommunication_win_threshold: int = DEFAULT_WIN_THRESHOLD
