#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel

from parrot.entity.game_instance import GameInstance


class GiveHintRequest(BaseModel):
    instance_id: str
    player_token: str
    hint: List[str]


class GiveHintResponse(BaseModel):
    instance: GameInstance
