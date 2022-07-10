#!/usr/bin/env python3

from typing import List

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relation, relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.game import Game
from parrot.entity.model.voting_mode import VotingMode


class GameInstance(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    instance_id = Column(String)
    guess_timeout = Column(Integer, nullable=False)
    voting_mode = Column(Enum(VotingMode))

    game_id = ForeignKey(Game.id)
    game = relationship(Game, uselist=False, foreign_keys=[game_id])

    def give_hint(self, player_token: str, hint: List[str]) -> None:
        raise NotImplementedError()

    def submit_guess(self, player_token: str, guess: List[int]) -> None:
        raise NotImplementedError()
