#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.model.game_instance import GameInstance


class StartLobbyRequest(BaseModel):
    instance_id: str
    player_token: str


class StartLobbyResponse(BaseModel):
    instance: GameInstance
