import random


class Hangman:
    words = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

    @staticmethod
    def hangman_test(obj, letter):
        if letter in obj['word']:
            i = obj['word'].find(letter)
            while i != -1:
                obj['mask'][i] = obj['word'][i]
                i = obj['word'].find(letter, i+1)
        else:
            obj['lives'] -= 1
        if '_' not in obj['mask']:
            obj['solved'] = True

        if letter not in obj['tested']:
            obj['tested'] += letter

        return obj

    def create_game(self):
        word = random.choice(self.words)
        return {'word': word, 'mask': list('_' * len(word)), 'solved': False, 'tested': '', 'lives': 5}
