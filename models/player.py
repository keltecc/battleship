#!/usr/bin/env python3

from abc import ABC, abstractmethod, abstractproperty
from random import randrange
from string import ascii_uppercase

from .cell import Cell
from .field import Field


class Player(ABC):
    @abstractproperty
    def field(self) -> Field:
        pass

    @abstractproperty
    def enemy_field(self) -> Field:
        pass
    
    @abstractmethod
    def get_shot(self) -> tuple:
        pass


class BasePlayer(Player):
    def __init__(self, field_width: int, field_height: int):
        self._field = Field(field_width, field_height)
        self._enemy_field = Field(field_width, field_height)
        return

    @property
    def field(self) -> Field:
        return self._field

    @property
    def enemy_field(self) -> Field:
        return self._enemy_field

    def get_shot(self) -> tuple:
        raise NotImplementedError


class AIPlayer(BasePlayer):
    def get_shot(self) -> tuple:
        return randrange(0, self._enemy_field.width), \
               randrange(0, self._enemy_field.height)


class ConsolePlayer(BasePlayer):
    def get_shot(self) -> tuple:
        line = input('Please, enter coordinates (ex. A 0): ')
        parts = line.split()
        x = ascii_uppercase.index(parts[0].upper())
        y = int(parts[1])
        return (x, y)
