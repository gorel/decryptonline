#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.game_lobby import GameLobby
from parrot.entity.model.player import Player


class JoinLobbyRequest(BaseModel):
    instance_id: str
    name: str


class JoinLobbyResponse(BaseModel):
    lobby: GameLobby
    player: Player
