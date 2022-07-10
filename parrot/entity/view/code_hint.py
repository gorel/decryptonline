#!/usr/bin/env python3

from typing import List


from pydantic import BaseModel


class CodeHint(BaseModel):
    indices: List[str]
