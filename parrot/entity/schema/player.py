#!/usr/bin/env python3

from pydantic import BaseModel


class Player(BaseModel):
    name: str
    is_captain: bool

    class Config:
        orm_mode = True


class PlayerCreate(Player):
    token: str

    class Config:
        orm_mode = True
