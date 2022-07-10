#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.code_hint import CodeHint
from parrot.entity.model.guess import Guess


class RoundNotes(ModelBase):
    id = Column(Integer, primary_key=True, index=True)

    code_hint_id = ForeignKey(CodeHint.id)
    team1_guess_id = ForeignKey(Guess.id)
    team2_guess_id = ForeignKey(Guess.id)

    code_hint = relationship(CodeHint, uselist=False, foreign_keys=[code_hint_id])
    team1_guess = relationship(Guess, uselist=False, foreign_keys=[team1_guess_id])
    team2_guess = relationship(Guess, uselist=False, foreign_keys=[team2_guess_id])
