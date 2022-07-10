#!/usr/bin/env python3

from sqlalchemy import Boolean, Column, Integer, String

from parrot.entity.database import ModelBase


class Player(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    token = Column(String)
    is_captain = Column(Boolean)
