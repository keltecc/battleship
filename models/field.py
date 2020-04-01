#!/usr/bin/env python3

from .cell import Cell


class Field(object):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._cells = [[Cell.EMPTY for x in range(self._width)] for y in range(self._height)]
        return

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    def __getitem__(self, xy: tuple) -> Cell:
        x, y = xy
        return self._cells[y][x]

    def __setitem__(self, xy: tuple, value: Cell):
        x, y = xy
        self._cells[y][x] = value
        return
