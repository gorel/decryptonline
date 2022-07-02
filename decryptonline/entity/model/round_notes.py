from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RoundNotes:
    code_words: List[str] = field(default_factory=list)
    my_team_guess: List[int] = field(default_factory=list)
    other_team_guess: List[int] = field(default_factory=list)
