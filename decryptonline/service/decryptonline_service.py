from decryptonline.service.storage import StorageService
from decryptonline.service.types import (
    CreateRequest,
    CreateResponse,
    GetRequest,
    GetResponse,
    UpdateRequest,
    UpdateResponse,
)


class DecryptonlineService:
    def __init__(self, storage_svc: StorageService) -> None:
        self.storage_svc = storage_svc

    def create(self, request: CreateRequest) -> CreateResponse:
        raise NotImplementedError()

    def get(self, request: GetRequest) -> GetResponse:
        raise NotImplementedError()

    def update(self, request: UpdateRequest) -> UpdateResponse:
        raise NotImplementedError()
