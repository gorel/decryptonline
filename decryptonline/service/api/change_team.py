#!/usr/bin/env python3

from dataclasses import dataclass

from decryptonline.entity.game_lobby import GameLobby


@dataclass
class ChangeTeamRequest:
    instance_id: str
    player_token: str


@dataclass
class ChangeTeamResponse:
    lobby: GameLobby
