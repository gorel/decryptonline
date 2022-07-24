#!/usr/bin/env python3

import dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from parrot.entity.database import ModelBase, get_engine, get_local_session
from parrot.service.api.change_team import ChangeTeamRequest, ChangeTeamResponse
from parrot.service.api.create_lobby import CreateLobbyRequest, CreateLobbyResponse
from parrot.service.api.get_instance import GetInstanceRequest, GetInstanceResponse
from parrot.service.api.get_lobby import GetLobbyRequest, GetLobbyResponse
from parrot.service.api.give_hint import GiveHintRequest, GiveHintResponse
from parrot.service.api.join_lobby import JoinLobbyRequest, JoinLobbyResponse
from parrot.service.api.start_lobby import StartLobbyRequest, StartLobbyResponse
from parrot.service.api.submit_guess import SubmitGuessRequest, SubmitGuessResponse
from parrot.service.parrot_service import ParrotService


dotenv.load_dotenv()


ModelBase.metadata.create_all(bind=get_engine())


app = FastAPI()
api = FastAPI(title="API")


app.mount("/api", api)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# Dependency
def get_db():
    db = get_local_session()
    try:
        yield db
    finally:
        db.close()


@api.get("/lobby/", response_model=GetLobbyResponse)
def get_lobby(
    request: GetLobbyRequest, db: Session = Depends(get_db)
) -> GetLobbyResponse:
    svc = ParrotService(db=db)
    return svc.get_lobby(request)


@api.post("/lobby/create", response_model=CreateLobbyResponse)
def create_lobby(
    request: CreateLobbyRequest, db: Session = Depends(get_db)
) -> CreateLobbyResponse:
    svc = ParrotService(db=db)
    return svc.create_lobby(request)


@api.post("/lobby/change_team", response_model=ChangeTeamResponse)
def change_team(
    request: ChangeTeamRequest, db: Session = Depends(get_db)
) -> ChangeTeamResponse:
    svc = ParrotService(db=db)
    return svc.change_team(request)


@api.post("/lobby/join", response_model=JoinLobbyResponse)
def join_lobby(
    request: JoinLobbyRequest, db: Session = Depends(get_db)
) -> JoinLobbyResponse:
    svc = ParrotService(db=db)
    return svc.join_lobby(request)


@api.post("/lobby/start", response_model=StartLobbyResponse)
def start_lobby(
    request: StartLobbyRequest, db: Session = Depends(get_db)
) -> StartLobbyResponse:
    svc = ParrotService(db=db)
    return svc.start_lobby(request)


@api.get("/instance/", response_model=GetInstanceResponse)
def get_instance(
    request: GetInstanceRequest, db: Session = Depends(get_db)
) -> GetInstanceResponse:
    svc = ParrotService(db=db)
    return svc.get_instance(request)


@api.post("/instance/give_hint", response_model=GiveHintResponse)
def give_hint(
    request: GiveHintRequest, db: Session = Depends(get_db)
) -> GiveHintResponse:
    svc = ParrotService(db=db)
    return svc.give_hint(request)


@api.post("/instance/guess", response_model=SubmitGuessResponse)
def submit_guess(
    request: SubmitGuessRequest, db: Session = Depends(get_db)
) -> SubmitGuessResponse:
    svc = ParrotService(db=db)
    return svc.submit_guess(request)
