from dataclasses import dataclass

from dataclasses_json import dataclass_json

from decryptonline.entity.model.team import Team


@dataclass_json
@dataclass
class Game:
    team1: Team
    team2: Team
