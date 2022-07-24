#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.schema.game_lobby import GameLobby
from parrot.entity.schema.player import PlayerCreate


class JoinLobbyRequest(BaseModel):
    instance_id: str
    name: str


class JoinLobbyResponse(BaseModel):
    lobby: GameLobby
    player: PlayerCreate
