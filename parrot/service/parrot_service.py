#!/usr/bin/env python3

from sqlalchemy.orm import Session

from parrot.entity.game_instance import GameInstance
from parrot.entity.game_lobby import GameLobby
from parrot.service.api.change_team import ChangeTeamRequest, ChangeTeamResponse
from parrot.service.api.create_lobby import CreateLobbyRequest, CreateLobbyResponse
from parrot.service.api.get_instance import GetInstanceRequest, GetInstanceResponse
from parrot.service.api.get_lobby import GetLobbyRequest, GetLobbyResponse
from parrot.service.api.give_hint import GiveHintRequest, GiveHintResponse
from parrot.service.api.join_lobby import JoinLobbyRequest, JoinLobbyResponse
from parrot.service.api.start_lobby import StartLobbyRequest, StartLobbyResponse
from parrot.service.api.submit_guess import SubmitGuessRequest, SubmitGuessResponse


class ParrotService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_lobby(self, request: CreateLobbyRequest) -> CreateLobbyResponse:
        instance_id = GameLobby._gen_new_instance_id()
        lobby = GameLobby(
            instance_id=instance_id,
            team1_name=request.team1_name,
            team2_name=request.team2_name,
            voting_mode=request.voting_mode,
            guess_timeout=request.guess_timeout,
        )
        self.db.add(lobby)
        self.db.commit()
        return CreateLobbyResponse(lobby=lobby)

    def change_team(self, request: ChangeTeamRequest) -> ChangeTeamResponse:
        lobby = GameLobby.get_by_instance_id(self.db, request.instance_id)
        lobby.change_team_for_player(request.player_token)
        self.db.commit()
        return ChangeTeamResponse(lobby=lobby)

    def get_instance(self, request: GetInstanceRequest) -> GetInstanceResponse:
        instance = GameInstance.get_by_instance_id(self.db, request.instance_id)
        return GetInstanceResponse(instance=instance)

    def get_lobby(self, request: GetLobbyRequest) -> GetLobbyResponse:
        lobby = GameLobby.get_by_instance_id(self.db, request.instance_id)
        return GetLobbyResponse(lobby=lobby)

    def give_hint(self, request: GiveHintRequest) -> GiveHintResponse:
        instance = GameInstance.get_by_instance_id(self.db, request.instance_id)
        instance.give_hint(request.player_token, request.hint)
        self.db.commit()
        return GiveHintResponse(instance=instance)

    def join_lobby(self, request: JoinLobbyRequest) -> JoinLobbyResponse:
        lobby = GameLobby.get_by_instance_id(self.db, request.instance_id)
        player = lobby.add_player(request.name)
        self.db.commit()
        return JoinLobbyResponse(lobby=lobby, player=player)

    def start_lobby(self, request: StartLobbyRequest) -> StartLobbyResponse:
        lobby = GameLobby.get_by_instance_id(self.db, request.instance_id)
        instance = lobby.create_instance_and_start()
        self.db.add(instance)
        self.db.commit()
        return StartLobbyResponse(instance=instance)

    def submit_guess(self, request: SubmitGuessRequest) -> SubmitGuessResponse:
        instance = GameInstance.get_by_instance_id(self.db, request.instance_id)
        instance.submit_guess(request.player_token, request.guess)
        self.db.commit()
        return SubmitGuessResponse(instance=instance)
