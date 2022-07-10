#!/usr/bin/env python3

from enum import Enum, auto


class GameStatus(Enum):
    TEAM1_PLAY = auto()
    TEAM2_PLAY = auto()
    TEAM1_WON = auto()
    TEAM2_WON = auto()
    DRAW = auto()
