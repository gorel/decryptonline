import abc
from typing import Generic, Optional, Type, TypeVar

Key = TypeVar("Key")
Value = TypeVar("Value")


class StorageService(Generic[Key, Value], abc.ABC):
    @abc.abstractmethod
    def read(self, entity_type: Type[Value], key: Key) -> Value:
        raise NotImplementedError()

    @abc.abstractmethod
    def write(
        self, key: Key, value: Value, entity_type: Optional[Type[Value]] = None
    ) -> None:
        raise NotImplementedError()
