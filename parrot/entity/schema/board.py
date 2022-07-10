#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel


class Board(BaseModel):
    cards: List[str]

    class Config:
        orm_mode = True
