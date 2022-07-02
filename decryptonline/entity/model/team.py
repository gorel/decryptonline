#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from decryptonline.entity.model.board import Board
from decryptonline.entity.model.player import Player


@dataclass_json
@dataclass
class Team:
    name: str
    board: Board
    players: List[Player]
    interception_tokens: int = 0
    miscommunication_tokens: int = 0
