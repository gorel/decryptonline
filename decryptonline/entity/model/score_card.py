from dataclasses import dataclass
from typing import List

from decryptonline.entity.model.round_notes import RoundNotes


@dataclass
class ScoreCard:
    team1_notes: List[RoundNotes]
    team2_notes: List[RoundNotes]
