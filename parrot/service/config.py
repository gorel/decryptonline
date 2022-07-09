#!/usr/bin/env python3

from __future__ import annotations

import importlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Type, TypeVar

from parrot.service.storage import StorageService


T = TypeVar("T")


class BadSubClassError(ValueError):
    def __init__(self, expected_class: Type, actual_class: Type) -> None:
        e_name = expected_class.__name__
        a_name = actual_class.__name__
        super().__init__(f"Expected a subclass of {e_name} but got {a_name}")


@dataclass
class ParrotServiceConfig:
    storage_svc: StorageService

    @classmethod
    def from_json(cls, json_filepath: Path) -> ParrotServiceConfig:
        with open(json_filepath) as f:
            data = json.load(f)

        storage_svc = cls._build_svc(StorageService, data["storage_svc"])
        return ParrotServiceConfig(storage_svc=storage_svc)

    @classmethod
    def _build_svc(cls, metatype: Type[T], d: Dict[str, Any]) -> T:
        # TODO: This belongs in a dedicated reflection class
        module_name, class_name = d["class"].rsplit(".", 1)
        module = importlib.import_module(module_name)
        real_cls = getattr(module, class_name)
        if not issubclass(real_cls, metatype):
            raise BadSubClassError(metatype, real_cls)

        kwargs = d["constructor"] or {}
        return real_cls(**kwargs)
