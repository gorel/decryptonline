#!/usr/bin/env python3

from dataclasses import dataclass

from dataclasses_json import dataclass_json

from decryptonline.entity.model.team import Team


@dataclass_json
@dataclass
class Player:
    name: str
    my_team: Team
