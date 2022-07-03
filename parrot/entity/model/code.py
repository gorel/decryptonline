#!/usr/bin/env python3

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from parrot.entity.model.board import Board
from parrot.entity.model.guess import Guess


@dataclass_json
@dataclass
class Code:
    indices: List[int]

    @classmethod
    def from_reference_board(cls, board: Board) -> Code:
        n = len(board.cards)
        return Code(random.sample(range(n), n))

    def check_guess(self, guess: Guess) -> bool:
        return self.indices == guess.indices