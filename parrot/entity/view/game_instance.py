#!/usr/bin/env python3

from typing import Optional

from pydantic import BaseModel

from parrot.entity.view.game import Game
from parrot.entity.model.voting_mode import VotingMode


class GameInstance(BaseModel):
    instance_id: str
    game: Game
    voting_mode: VotingMode
    guess_timeout: Optional[int]
