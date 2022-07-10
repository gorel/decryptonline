#!/usr/bin/env python3

import json
from typing import List

from sqlalchemy import Column, Integer, String

from parrot.entity.database import ModelBase


class Board(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    cards_db_str = Column(String)

    @property
    def cards(self) -> List[str]:
        key = self.cards_db_str
        assert isinstance(key, str)
        return json.loads(key)

    @cards.setter
    def cards(self, value: List[str]) -> None:
        self.cards_db_str = json.dumps(value)
