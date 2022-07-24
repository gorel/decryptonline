#!/usr/bin/env python3

from __future__ import annotations

import random
import string
from typing import Tuple

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

from parrot.entity.database import ModelBase
from parrot.entity.errors import PlayerNotFoundError
from parrot.entity.model.board import Board
from parrot.entity.model.game import Game
from parrot.entity.model.game_instance import GameInstance
from parrot.entity.model.player import Player
from parrot.entity.model.team import Team
from parrot.entity.schema.game_status import GameStatus
from parrot.entity.schema.voting_mode import VotingMode


INSTANCE_ID_LEN = 4
LEN_NEW_PLAYER_TOKEN = 12


class GameLobby(ModelBase):
    __tablename__ = "game_lobby"

    instance_id = Column(String, primary_key=True, index=True)
    team1_name = Column(String, nullable=False)
    team2_name = Column(String, nullable=False)
    voting_mode = Column(Enum(VotingMode), nullable=False)
    started = Column(Boolean, nullable=False)
    guess_timeout = Column(Integer)

    team1_player_id = ForeignKey(Player.id)
    team2_player_id = ForeignKey(Player.id)

    team1_players = relationship(Player, foreign_keys=[team1_player_id])
    team2_players = relationship(Player, foreign_keys=[team2_player_id])

    @classmethod
    def get_by_instance_id(cls, db: Session, instance_id: str) -> GameLobby:
        return db.query(cls).filter(cls.instance_id == instance_id).first()

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
        player = Player(
            name=player_name, is_captain=False, token=self._gen_new_player_token()
        )
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
        words = ["foo"]
        boards = Board(words[: len(words) // 2]), Board(words[len(words) // 2 :])
        raise NotImplementedError()

    @classmethod
    def gen_new_instance_id(cls, db: Session, length: int = INSTANCE_ID_LEN) -> str:
        candidate_id = "".join(
            random.choice(string.ascii_uppercase) for _ in range(length)
        )
        # Keep going until we don't have a collision
        while cls.get_by_instance_id(db, candidate_id) is not None:
            candidate_id = "".join(
                random.choice(string.ascii_uppercase) for _ in range(length)
            )
        return candidate_id

    @classmethod
    def _gen_new_player_token(cls) -> str:
        return "".join(
            random.choice(string.hexdigits) for _ in range(LEN_NEW_PLAYER_TOKEN)
        )
