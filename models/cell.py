#!/usr/bin/env python3

from enum import Enum


class Cell(Enum):
    EMPTY = 0
    ALIVE = 1
    DEAD = 2
    SHOT = 3
