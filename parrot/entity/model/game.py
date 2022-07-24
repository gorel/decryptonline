#!/usr/bin/env python3

from sqlalchemy import Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.score_card import ScoreCard
from parrot.entity.model.team import Team
from parrot.entity.schema.game_status import GameStatus


class Game(ModelBase):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(GameStatus))
    round = Column(Integer)
    interception_win_threshold = Column(Integer)
    miscommunication_win_threshold = Column(Integer)

    team1_id = Column(Integer, ForeignKey(Team.id))
    team2_id = Column(Integer, ForeignKey(Team.id))
    score_card_id = Column(Integer, ForeignKey(ScoreCard.id))

    team1 = relationship(Team, uselist=False, foreign_keys=[team1_id])
    team2 = relationship(Team, uselist=False, foreign_keys=[team2_id])
    score_card = relationship(ScoreCard, uselist=False, foreign_keys=[score_card_id])
