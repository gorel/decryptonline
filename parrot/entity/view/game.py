#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.view.score_card import ScoreCard
from parrot.entity.view.team import Team
from parrot.entity.model.game import GameStatus


class Game(BaseModel):
    status: GameStatus
    round: int
    interception_win_threshold: int
    miscommunication_win_threshold: int
    team1: Team
    team2: Team
    score_card: ScoreCard
