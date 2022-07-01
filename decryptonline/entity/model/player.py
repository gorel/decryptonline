from dataclasses import dataclass

from decryptonline.entity.model.team import Team


@dataclass
class Player:
    name: str
    my_team: Team
