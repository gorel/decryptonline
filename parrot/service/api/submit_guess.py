#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel

from parrot.entity.game_instance import GameInstance


class SubmitGuessRequest(BaseModel):
    instance_id: str
    player_token: str
    guess: List[int]


class SubmitGuessResponse(BaseModel):
    instance: GameInstance
