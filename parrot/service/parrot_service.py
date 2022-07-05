#!/usr/bin/env python3

import random
import string

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
from parrot.service.storage import StorageService


INSTANCE_ID_LEN = 4


class ParrotService:
    def __init__(self, storage_svc: StorageService) -> None:
        self.storage_svc = storage_svc

    def change_team(self, request: ChangeTeamRequest) -> ChangeTeamResponse:
        lobby = self.storage_svc.read(entity_type=GameLobby, key=request.instance_id)
        lobby.change_team_for_player(request.player_token)
        self.storage_svc.write(key=request.instance_id, value=lobby)
        return ChangeTeamResponse(lobby=lobby)

    def create_lobby(self, request: CreateLobbyRequest) -> CreateLobbyResponse:
        instance_id = self._gen_new_instance_id()
        lobby = GameLobby(
            instance_id=instance_id,
            team1_name=request.team1_name,
            team2_name=request.team2_name,
            voting_mode=request.voting_mode,
            guess_timeout=request.guess_timeout,
        )
        self.storage_svc.write(key=instance_id, value=lobby)
        return CreateLobbyResponse(lobby=lobby)

    def get_instance(self, request: GetInstanceRequest) -> GetInstanceResponse:
        instance = self.storage_svc.read(
            entity_type=GameInstance, key=request.instance_id
        )
        return GetInstanceResponse(instance=instance)

    def get_lobby(self, request: GetLobbyRequest) -> GetLobbyResponse:
        lobby = self.storage_svc.read(entity_type=GameLobby, key=request.instance_id)
        return GetLobbyResponse(lobby=lobby)

    def give_hint(self, request: GiveHintRequest) -> GiveHintResponse:
        instance = self.storage_svc.read(
            entity_type=GameInstance, key=request.instance_id
        )
        instance.give_hint(request.player_token, request.hint)
        self.storage_svc.write(key=request.instance_id, value=instance)
        return GiveHintResponse(instance=instance)

    def join_lobby(self, request: JoinLobbyRequest) -> JoinLobbyResponse:
        lobby = self.storage_svc.read(entity_type=GameLobby, key=request.instance_id)
        player = lobby.add_player(request.name)
        self.storage_svc.write(key=request.instance_id, value=lobby)
        return JoinLobbyResponse(lobby=lobby, player=player)

    def start_lobby(self, request: StartLobbyRequest) -> StartLobbyResponse:
        lobby = self.storage_svc.read(entity_type=GameLobby, key=request.instance_id)
        instance = lobby.create_instance_and_start()

        self.storage_svc.write(key=request.instance_id, value=instance)
        self.storage_svc.write(key=request.instance_id, value=lobby)
        return StartLobbyResponse(instance=instance)

    def submit_guess(self, request: SubmitGuessRequest) -> SubmitGuessResponse:
        instance = self.storage_svc.read(
            entity_type=GameInstance, key=request.instance_id
        )
        instance.submit_guess(request.player_token, request.guess)
        self.storage_svc.write(key=request.instance_id, value=instance)
        return SubmitGuessResponse(instance=instance)

    def _gen_new_instance_id(self) -> str:
        # TODO: Check storage_svc to ensure this instance doesn't exist already
        return "".join(
            random.choice(string.ascii_uppercase) for _ in range(INSTANCE_ID_LEN)
        )
