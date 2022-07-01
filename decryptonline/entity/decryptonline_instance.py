from __future__ import annotations


class GameInstance:
    instance_id: int

    def __init__(self) -> None:
        pass

    def dumps(self) -> str:
        raise NotImplementedError()

    @classmethod
    def loads(cls, json_str: str) -> GameInstance:
        raise NotImplementedError()
