#!/usr/bin/env python3

from random import randint

from models.cell import Cell
from models.field import Field


class FieldFiller(object):
    @staticmethod
    def fill_with_ships(field: Field):
        # set first 4-cell ship
        field[0, 0] = Cell.ALIVE
        field[1, 0] = Cell.ALIVE
        field[2, 0] = Cell.ALIVE
        field[3, 0] = Cell.ALIVE

        # set first 3-cell ship
        field[0, 2] = Cell.ALIVE
        field[1, 2] = Cell.ALIVE
        field[2, 2] = Cell.ALIVE

        # set second 3-cell ship
        field[0, 4] = Cell.ALIVE
        field[1, 4] = Cell.ALIVE
        field[2, 4] = Cell.ALIVE

        #set first 2-cell ship
        field[4, 3] = Cell.ALIVE
        field[4, 4] = Cell.ALIVE

        #set random 1-cell ships
        for x in range(6, field.width, 2):
            for y in range(0, field.height, 2):
                if randint(0, 10) > 3:
                    field[x, y] = Cell.ALIVE
        for x in range(0, 6, 2):
            for y in range(6, field.height, 2):
                if randint(0, 10) > 3:
                    field[x, y] = Cell.ALIVE

        return
