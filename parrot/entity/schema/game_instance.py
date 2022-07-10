#!/usr/bin/env python3

from typing import Optional

from pydantic import BaseModel

from parrot.entity.model.voting_mode import VotingMode
from parrot.entity.schema.game import Game


class GameInstance(BaseModel):
    instance_id: str
    game: Game
    voting_mode: VotingMode
    guess_timeout: Optional[int]

    class Config:
        orm_mode = True
