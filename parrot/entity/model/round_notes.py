#!/usr/bin/env python3

from dataclasses import dataclass

from dataclasses_json import dataclass_json

from parrot.entity.model.code_hint import CodeHint
from parrot.entity.model.guess import Guess


@dataclass_json
@dataclass
class RoundNotes:
    code_hint: CodeHint
    team1_guess: Guess
    team2_guess: Guess
