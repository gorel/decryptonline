
from dataclasses import dataclass
from typing import List


@dataclass
class RoundNotes:
    code_words: List[str]
    my_team_guess: List[int]
    other_team_guess: List[int]
