#!/usr/bin/env python3

from pydantic import BaseModel


from parrot.entity.view.code_hint import CodeHint
from parrot.entity.view.guess import Guess


class RoundNotes(BaseModel):
    code_hint: CodeHint
    team1_guess: Guess
    team2_guess: Guess
