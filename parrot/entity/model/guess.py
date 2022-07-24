#!/usr/bin/env python3

import json
from typing import List

from sqlalchemy import Column, Integer, String

from parrot.entity.database import ModelBase


class Guess(ModelBase):
    __tablename__ = "guess"

    id = Column(Integer, primary_key=True, index=True)
    indices_db_str = Column(String)

    @property
    def indices(self) -> List[int]:
        key = self.indices_db_str
        assert isinstance(key, str)
        return json.loads(key)

    @indices.setter
    def indices(self, value: List[int]) -> None:
        self.indices_db_str = json.dumps(value)
