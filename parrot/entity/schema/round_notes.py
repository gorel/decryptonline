#!/usr/bin/env python3

from pydantic import BaseModel


from parrot.entity.schema.code_hint import CodeHint
from parrot.entity.schema.guess import Guess


class RoundNotes(BaseModel):
    code_hint: CodeHint
    team1_guess: Guess
    team2_guess: Guess

    class Config:
        orm_mode = True
