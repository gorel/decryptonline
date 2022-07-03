#!/usr/bin/env python3

from dataclasses import dataclass

from decryptonline.entity.game_instance import GameInstance


@dataclass
class StartLobbyRequest:
    instance_id: str
    player_token: str


@dataclass
class StartLobbyResponse:
    game: GameInstance
