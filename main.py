#!/usr/bin/env python3

from argparse import ArgumentParser

from draw import FieldDrawer
from helpers import FieldFiller
from serializer import GameSerializer

from models.game import Game
from models.player import ConsolePlayer, AIPlayer


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('--width', type=int, choices=range(5, 20), default=10, help='game field width')
    parser.add_argument('--height', type=int, choices=range(5, 20), default=10, help='game field height')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--first-player', action='store_true', default=None, help='be the first player')
    group.add_argument('--second-player', action='store_true', default=None, help='be the second player')

    return parser.parse_args()


def create_game() -> tuple:
    args = parse_args()
    
    if GameSerializer.is_saved_game_exists():
        choice = input('Saved game exists. Do you want to load it? (y/n): ')
        if choice[0].lower() == 'y':
            return GameSerializer.load_game()
    
    console_player = ConsolePlayer(args.width, args.height)
    ai_player = AIPlayer(args.width, args.height)

    FieldFiller.fill_with_ships(console_player.field)
    FieldFiller.fill_with_ships(ai_player.field)

    if args.second_player:
        game = Game(ai_player, console_player)
    else:
        game = Game(console_player, ai_player)

    return console_player, game


def main():
    console_player, game = create_game()

    try:
        while game.winner is None:
            print('Your field:')
            FieldDrawer.draw_field(console_player.field)
            print('Enemy field:')
            FieldDrawer.draw_field(console_player.enemy_field)
            game.step()
    except KeyboardInterrupt:
        print()
        choice = input('Do you want to save the game? (y/n): ')
        if choice[0].lower() == 'y':
            GameSerializer.save_game(console_player, game)
        return

    if isinstance(game.winner, ConsolePlayer):
        print('You win!')
    else:
        print('You lose!')
    return


if __name__ == '__main__':
    main()
