#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json

from parrot.entity.model.round_notes import RoundNotes


@dataclass_json
@dataclass
class ScoreCard:
    team1_notes: List[RoundNotes] = field(default_factory=list)
    team2_notes: List[RoundNotes] = field(default_factory=list)