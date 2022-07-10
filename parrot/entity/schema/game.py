#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.model.game import GameStatus
from parrot.entity.schema.score_card import ScoreCard
from parrot.entity.schema.team import Team


class Game(BaseModel):
    status: GameStatus
    round: int
    interception_win_threshold: int
    miscommunication_win_threshold: int
    team1: Team
    team2: Team
    score_card: ScoreCard

    class Config:
        orm_mode = True
