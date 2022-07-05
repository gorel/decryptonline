#!/usr/bin/env python3

import random
import string
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from dataclasses_json import dataclass_json

from parrot.entity.errors import PlayerNotFoundError
from parrot.entity.model.board import Board
from parrot.entity.model.card import Card
from parrot.entity.model.game import Game, GameStatus
from parrot.entity.model.player import Player
from parrot.entity.model.team import Team
from parrot.entity.model.voting_mode import VotingMode
from parrot.entity.game_instance import GameInstance


LEN_NEW_PLAYER_TOKEN = 12


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
        # Check in team 1
        for i, player in enumerate(self.team1_players):
            if player.token == player_token:
                if len(self.team2_players) == 0:
                    # This player will be the captain now
                    player.is_captain = True
                else:
                    player.is_captain = False
                self.team2_players.append(player)
                del self.team1_players[i]
                return

        # Check in team 2
        for i, player in enumerate(self.team2_players):
            if player.token == player_token:
                if len(self.team1_players) == 0:
                    # This player will be the captain now
                    player.is_captain = True
                else:
                    player.is_captain = False
                self.team1_players.append(player)
                del self.team2_players[i]
                return

        raise PlayerNotFoundError(player_token)

    def add_player(self, player_name: str) -> None:
        player = Player(name=player_name, is_captain=False, token=self._gen_new_player_token())
        if len(self.team1_players) == 0:
            player.is_captain = True
            self.team1_players.append(player)
        elif len(self.team2_players) == 0:
            player.is_captain = True
            self.team2_players.append(player)
        elif len(self.team1_players) <= len(self.team2_players):
            self.team1_players.append(player)
        else:
            self.team2_players.append(player)

    def create_instance_and_start(self) -> GameInstance:
        board1, board2 = self._gen_two_boards()
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
        boards = Board(words[: len(words) // 2]), Board(words[len(words) // 2 :])
        raise NotImplementedError()

    def _gen_new_player_token(self) -> str:
    return "".join(random.choice(string.hexdigits) for _ in range(LEN_NEW_PLAYER_TOKEN))
