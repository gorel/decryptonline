#!/usr/bin/env python3

from dataclasses import dataclass

from parrot.entity.game_instance import GameInstance


@dataclass
class GetInstanceRequest:
    instance_id: str


@dataclass
class GetInstanceResponse:
    instance: GameInstance
