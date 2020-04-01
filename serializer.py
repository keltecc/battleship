#!/usr/bin/env python3

import pickle
import os.path

from models.game import Game
from models.field import Field
from models.player import ConsolePlayer


class GameSerializer(object):
    FILENAME = 'save.dat'

    @staticmethod
    def is_saved_game_exists():
        return os.path.isfile(GameSerializer.FILENAME)

    @staticmethod
    def save_game(console_player: ConsolePlayer, game: Game):
        with open(GameSerializer.FILENAME, 'wb') as file:
            pickle.dump((console_player, game), file)
        return

    @staticmethod
    def load_game() -> tuple:
        with open(GameSerializer.FILENAME, 'rb') as file:
            return pickle.load(file)
