#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.game_instance import GameInstance


class GetInstanceRequest(BaseModel):
    instance_id: str


class GetInstanceResponse(BaseModel):
    instance: GameInstance
