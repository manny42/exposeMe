import random


class Hangman:
	words = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

	def __init__(self, word="", mask="", solved=False, tested="", lives=5):
		self.word = word if word else random.choice(self.words)
		self.mask = mask if mask else list('_' * len(self.word))
		self.solved = solved
		self.tested = tested
		self.lives = lives

	@classmethod
	def from_json(cls, json):
		return cls(json.word, json.mask, json.solved, json.tested, json.lives)

	@classmethod
	def from_dict(cls, dict):
		return cls(dict['word'], dict['mask'], dict['solved'], dict['tested'], dict['lives'])

	def to_json(self):
		return {'word': self.word, 'mask': self.mask, 'solved': self.solved, 'tested': self.tested, 'lives': self.lives}

	def test_letter(self, letter):
		print("Testing letter: {}, and the word is: {}".format(letter, self.word))
		if letter in self.word:
			i = self.word.find(letter)
			while i != -1:
				self.mask[i] = self.word[i]
				i = self.word.find(letter, i+1)
		else:
			self.lives -= 1

		print("The mask is: {}".format(self.mask))

		if '_' not in self.mask:
			self.solved = True

		if letter not in self.tested:
			self.tested += letter

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

	def create_game(self, word=""):
		if not word:
			word = random.choice(self.words)
		return {'word': word, 'mask': list('_' * len(word)), 'solved': False, 'tested': '', 'lives': 5}
