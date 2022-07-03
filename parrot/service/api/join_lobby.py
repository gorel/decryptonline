#!/usr/bin/env python3

from dataclasses import dataclass

from parrot.entity.game_lobby import GameLobby
from parrot.entity.model.player import Player


@dataclass
class JoinLobbyRequest:
    instance_id: str
    name: str


@dataclass
class JoinLobbyResponse:
    lobby: GameLobby
    player: Player
