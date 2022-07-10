#!/usr/bin/env python3

from pydantic import BaseModel


class Player(BaseModel):
    name: str
    token: str
    is_captain: bool
