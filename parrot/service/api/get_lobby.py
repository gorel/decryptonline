#!/usr/bin/env python3

from dataclasses import dataclass

from parrot.entity.game_lobby import GameLobby


@dataclass
class GetLobbyRequest:
    instance_id: str


@dataclass
class GetLobbyResponse:
    lobby: GameLobby
