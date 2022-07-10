#!/usr/bin/env python3

from __future__ import annotations

from typing import List

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.game import Game
from parrot.entity.model.voting_mode import VotingMode


class GameInstance(ModelBase):
    instance_id = Column(String, primary_key=True, index=True)
    guess_timeout = Column(Integer, nullable=False)
    voting_mode = Column(Enum(VotingMode))

    game_id = ForeignKey(Game.id)
    game = relationship(Game, uselist=False, foreign_keys=[game_id])

    @classmethod
    def get_by_instance_id(cls, db: Session, instance_id: str) -> GameInstance:
        return db.query(cls).filter(cls.instance_id == instance_id).first()

    def give_hint(self, player_token: str, hint: List[str]) -> None:
        raise NotImplementedError()

    def submit_guess(self, player_token: str, guess: List[int]) -> None:
        raise NotImplementedError()
