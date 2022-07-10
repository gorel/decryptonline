#!/usr/bin/env python3


from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.round_notes import RoundNotes


class ScoreCard(ModelBase):
    id = Column(Integer, primary_key=True, index=True)

    team1_notes_id = ForeignKey(RoundNotes.id)
    team2_notes_id = ForeignKey(RoundNotes.id)

    team1_notes = relationship(RoundNotes, foreign_keys=[team1_notes_id])
    team2_notes = relationship(RoundNotes, foreign_keys=[team2_notes_id])
