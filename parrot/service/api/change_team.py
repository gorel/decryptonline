#!/usr/bin/env python3

from pydantic import BaseModel

from parrot.entity.model.game_lobby import GameLobby


class ChangeTeamRequest(BaseModel):
    instance_id: str
    player_token: str


class ChangeTeamResponse(BaseModel):
    lobby: GameLobby
