#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from decryptonline.entity.model.player import Player


@dataclass_json
@dataclass
class GameLobby:
    instance_id: str
    team1_name: str
    team2_name: str
    team1_players: List[Player]
    team2_players: List[Player]
