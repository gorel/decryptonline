#!/usr/bin/env python3

from typing import Optional

from pydantic import BaseModel

from parrot.entity.schema.game_lobby import GameLobby
from parrot.entity.schema.voting_mode import VotingMode


class CreateLobbyRequest(BaseModel):
    team1_name: str
    team2_name: str
    voting_mode: VotingMode
    guess_timeout: Optional[int]


class CreateLobbyResponse(BaseModel):
    lobby: GameLobby
