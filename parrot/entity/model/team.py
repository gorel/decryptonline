#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from parrot.entity.database import ModelBase
from parrot.entity.model.board import Board
from parrot.entity.model.player import Player


class Team(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    interception_tokens = Column(Integer)
    miscommunication_tokens = Column(Integer)

    board_id = ForeignKey(Board.id)
    player_id = ForeignKey(Player.id)

    board = relationship(Board, uselist=False, foreign_keys=[board_id])
    players = relationship(Player, foreign_keys=[player_id])
