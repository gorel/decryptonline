#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from parrot.entity.game_instance import GameInstance


@dataclass
class GiveHintRequest:
    instance_id: str
    player_token: str
    hint: List[str]


@dataclass
class GiveHintResponse:
    instance: GameInstance
