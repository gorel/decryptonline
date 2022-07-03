#!/usr/bin/env python3

from dataclasses import dataclass
from enum import Enum, auto

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class VotingMode(Enum):
    DICTATORSHIP = auto()
    DEMOCRACY = auto()
