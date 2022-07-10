#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel, Field

from parrot.entity.schema.round_notes import RoundNotes


class ScoreCard(BaseModel):
    team1_notes: List[RoundNotes] = Field(default_factory=list)
    team2_notes: List[RoundNotes] = Field(default_factory=list)

    class Config:
        orm_mode = True
