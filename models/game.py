#!/usr/bin/env python3

from .cell import Cell
from .player import Player


class Game(object):
    def __init__(self, player1: Player, player2: Player):
        self._player1, self._player2 = player1, player2
        return

    @property
    def winner(self) -> Player:
        if Game._is_player_loser(self._player1):
            return self._player2
        if Game._is_player_loser(self._player2):
            return self._player1
        return None

    def step(self):
        Game._make_shot(self._player1, self._player2)
        Game._make_shot(self._player2, self._player1)
        return

    @staticmethod
    def _make_shot(attacker: Player, defender: Player):
        shot = attacker.get_shot()
        if defender.field[shot] == Cell.ALIVE:
            defender.field[shot] = Cell.DEAD
            attacker.enemy_field[shot] = Cell.DEAD
        elif defender.field[shot] == Cell.EMPTY:
            defender.field[shot] = Cell.SHOT
            attacker.enemy_field[shot] = Cell.SHOT
        return

    @staticmethod
    def _is_player_loser(player: Player) -> bool:
        return all(player.field[x, y] != Cell.ALIVE 
                    for x in range(player.field.width) 
                    for y in range(player.field.height))
