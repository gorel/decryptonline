#!/usr/bin/env python3

from typing import List

from pydantic import BaseModel


class Guess(BaseModel):
    indices: List[int]
