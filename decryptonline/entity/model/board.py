from dataclasses import dataclass
from typing import List

from decryptonline.entity.model.card import Card


@dataclass
class Board:
    cards: List[Card]
