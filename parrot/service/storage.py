import abc
from typing import Generic, TypeVar

Key = TypeVar("Key")
Value = TypeVar("Value")


class StorageService(Generic[Key, Value], abc.ABC):
    @abc.abstractmethod
    def read(self, entity_name: str, key: Key) -> Value:
        raise NotImplementedError()

    @abc.abstractmethod
    def write(self, entity_name: str, key: Key, value: Value) -> None:
        raise NotImplementedError()
