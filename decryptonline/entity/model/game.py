from dataclasses import dataclass

from decryptonline.entity.model.team import Team


@dataclass
class Game:
    team1: Team
    team2: Team
