#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json

from parrot.entity.model.game import Game
from parrot.entity.model.voting_mode import VotingMode


@dataclass_json
@dataclass
class GameInstance:
    instance_id: str
    game: Game
    voting_mode: VotingMode
    guess_timeout: Optional[int]

    def give_hint(self, player_token: str, hint: List[str]) -> None:
        raise NotImplementedError()

    def submit_guess(self, player_token: str, guess: List[int]) -> None:
        raise NotImplementedError()
