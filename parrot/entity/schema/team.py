#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel

from parrot.entity.schema.board import Board
from parrot.entity.schema.player import Player


class Team(BaseModel):
    name: str
    board: Board
    players: List[Player]
    interception_tokens: int = 0
    miscommunication_tokens: int = 0

    class Config:
        orm_mode = True
