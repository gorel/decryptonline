#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.model.game_lobby import GameLobby


class GetLobbyRequest(BaseModel):
    instance_id: str


class GetLobbyResponse(BaseModel):
    lobby: GameLobby
