#!/usr/bin/env python3

from __future__ import annotations

import random
from typing import List

from pydantic import BaseModel

from parrot.entity.view.board import Board
from parrot.entity.view.guess import Guess


class Code(BaseModel):
    indices: List[int]

    @classmethod
    def from_reference_board(cls, board: Board) -> Code:
        n = len(board.cards)
        return Code(random.sample(range(n), n))

    def check_guess(self, guess: Guess) -> bool:
        return self.indices == guess.indices
