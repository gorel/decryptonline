#!/usr/bin/env python3

from dataclasses import dataclass
from enum import Enum, auto

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GameStatus(Enum):
    TEAM1_PLAY = auto()
    TEAM2_PLAY = auto()
    TEAM1_WON = auto()
    TEAM2_WON = auto()
    DRAW = auto()
