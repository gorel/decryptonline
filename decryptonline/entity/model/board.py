#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from decryptonline.entity.model.card import Card


@dataclass_json
@dataclass
class Board:
    cards: List[Card]
