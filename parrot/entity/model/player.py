#!/usr/bin/env python3

from sqlalchemy import Boolean, Column, Integer, String

from parrot.entity.database import ModelBase


class Player(ModelBase):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    token = Column(String, index=True)
    is_captain = Column(Boolean)
