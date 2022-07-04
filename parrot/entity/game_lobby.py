#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from dataclasses_json import dataclass_json

from parrot.entity.model.board import Board
from parrot.entity.model.card import Card
from parrot.entity.model.game import Game, GameStatus
from parrot.entity.model.player import Player
from parrot.entity.model.team import Team
from parrot.entity.model.voting_mode import VotingMode
from parrot.entity.game_instance import GameInstance


@dataclass_json
@dataclass
class GameLobby:
    instance_id: str
    team1_name: str
    team2_name: str
    voting_mode: VotingMode
    guess_timeout: Optional[int]
    team1_players: List[Player] = field(default_factory=list)
    team2_players: List[Player] = field(default_factory=list)
    started: bool = False

    def change_team_for_player(self, player_token: str) -> None:
        raise NotImplementedError()

    def add_player(self, player_name: str) -> None:
        raise NotImplementedError()

    def create_instance_and_start(self) -> GameInstance:
        board1, board2 = self._gen_two_boards()
        board1, board2 = Board.create_two_from_lobby()
        game = Game(
            status=GameStatus.TEAM1_PLAY,
            team1=Team(name=self.team1_name, board=board1, players=self.team1_players),
            team2=Team(name=self.team2_name, board=board2, players=self.team2_players),
        )
        self.started = True
        return GameInstance(
            instance_id=self.instance_id,
            game=game,
            voting_mode=self.voting_mode,
            guess_timeout=self.guess_timeout,
        )

    def _gen_two_boards(self) -> Tuple[Board, Board]:
        # TODO: Look up number of words * 2
        words = [Card("foo")]
        return Board(words[: len(words) // 2]), Board(words[len(words) // 2 :])
