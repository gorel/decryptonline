from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from decryptonline.entity.model.board import Board


@dataclass_json
@dataclass
class Code:
    indices: List[int]

    @classmethod
    def from_reference_board(cls, board: Board) -> Code:
        n = len(board.cards)
        return Code(random.sample(range(n), n))
