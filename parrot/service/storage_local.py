#!/usr/bin/env python3

import os
import pathlib
from typing import Generic, Optional, Type, TypeVar

from dataclasses_json import dataclass_json

from parrot.service.storage import StorageService

Key = TypeVar("Key")
Value = TypeVar("Value", bound=dataclass_json)


class LocalStorageService(StorageService):
    def __init__(self) -> None:
        self.root = pathlib.Path(
            os.getenv("LOCAL_STORAGE_SERVICE_ROOT", pathlib.Path(__file__).parent)
        )

    def read(self, entity_type: Type[Value], key: Key) -> Value:
        with open(self.root / str(key)) as f:
            return entity_type.schema().loads(f.read())

    def write(
        self, key: Key, value: Value, entity_type: Optional[Type[Value]] = None
    ) -> None:
        entity_type = entity_type or value.__class__
        # Needed to appease the type checker
        assert entity_type is not None
        with open(self.root / str(key), "w") as f:
            f.write(entity_type.schema().dump(value))
