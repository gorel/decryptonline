#!/usr/bin/env python3

import json
from typing import List

from sqlalchemy import Column, Integer, String

from parrot.entity.database import ModelBase


class CodeHint(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    hint_db_str = Column(String)

    @property
    def hint(self) -> List[str]:
        key = self.hint_db_str
        assert isinstance(key, str)
        return json.loads(key)

    @hint.setter
    def hint(self, value: List[str]) -> None:
        self.hint_db_str = json.dumps(value)
