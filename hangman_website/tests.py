from django.test import TestCase

from .utils import Hangman


class HangmanMethodTests(TestCase):

    def test_creation_of_hangman(self):
        """
        create_game() should return a game that will be stored in session
        """
        game = Hangman().create_game()
        self.assertEqual(game['mask'], ['_'] * len(game['word']))
        self.assertEqual(game['solved'], False)
        self.assertEqual(game['tested'], '')
        self.assertEqual(game['lives'], 5)

    def test_game_winning(self):
        """
        Test case where we find the word right away
        """
        game = get_specific_word()
        game = Hangman.hangman_test(game, '3')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3',
                                'lives': 5})
        game = Hangman.hangman_test(game, 'd')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', 'd', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3d',
                                'lives': 5})
        game = Hangman.hangman_test(game, 'h')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', 'd', 'h', '_', '_', '_'],
                                'solved': False,
                                'tested': '3dh',
                                'lives': 5})
        game = Hangman.hangman_test(game, 'u')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', 'd', 'h', 'u', '_', '_'],
                                'solved': False,
                                'tested': '3dhu',
                                'lives': 5})
        game = Hangman.hangman_test(game, 'b')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', 'd', 'h', 'u', 'b', '_'],
                                'solved': False,
                                'tested': '3dhub',
                                'lives': 5})
        game = Hangman.hangman_test(game, 's')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', 'd', 'h', 'u', 'b', 's'],
                                'solved': True,
                                'tested': '3dhubs',
                                'lives': 5})

    def test_game_loose(self):
        """
        Test where we loose the game and find only one letter
        """
        game = get_specific_word()
        game = Hangman.hangman_test(game, '3')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3',
                                'lives': 5})
        game = Hangman.hangman_test(game, 'g')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3g',
                                'lives': 4})
        game = Hangman.hangman_test(game, 'j')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3gj',
                                'lives': 3})
        game = Hangman.hangman_test(game, 'l')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3gjl',
                                'lives': 2})
        game = Hangman.hangman_test(game, 't')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3gjlt',
                                'lives': 1})
        game = Hangman.hangman_test(game, 'p')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3gjltp',
                                'lives': 0})

    def test_double_play(self):
        game = get_specific_word()
        game = Hangman.hangman_test(game, '3')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3',
                                'lives': 5})
        game = Hangman.hangman_test(game, '3')
        self.assertEqual(game, {'word': '3dhubs',
                                'mask': ['3', '_', '_', '_', '_', '_'],
                                'solved': False,
                                'tested': '3',
                                'lives': 5})


def get_specific_word(word='3dhubs'):
    hangman = Hangman()
    game = hangman.create_game()
    while game['word'] != word:
        game = hangman.create_game()
    return game