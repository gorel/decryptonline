#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from decryptonline.entity.game_instance import GameInstance


@dataclass
class SubmitGuessRequest:
    instance_id: str
    player_token: str
    guess: List[int]


@dataclass
class SubmitGuessResponse:
    instance: GameInstance
