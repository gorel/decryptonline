#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from decryptonline.entity.model.game import Game
from decryptonline.entity.model.voting_mode import VotingMode


@dataclass_json
@dataclass
class GameInstance:
    instance_id: str
    game: Game
    voting_mode: VotingMode
    guess_timeout: Optional[int]
