#!/usr/bin/env python3

from string import ascii_uppercase

from models.cell import Cell
from models.field import Field


class FieldDrawer(object):
    SYMBOLS = {
        Cell.EMPTY: '.',
        Cell.ALIVE: 'O',
        Cell.DEAD: 'X',
        Cell.SHOT: '*'
    }

    @staticmethod
    def draw_field(field: Field):
        print('  ' + ' '.join(ascii_uppercase[:field.width]))
        for y in range(field.height):
            line = (field[x, y] for x in range(field.width))
            print(f'{y} ' + ' '.join(map(FieldDrawer.SYMBOLS.get, line)))
        print()
