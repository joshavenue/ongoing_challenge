import math
import random
import os
from nltk.tokenize import word_tokenize

def system_clean():

	if os.system == 'posix':
		os.system('clr')
	else:
		os.system('clear')

def display_text():

	print(texts())

def tokenizer():

	time = 0
	global empty
	empty = []

	while time < 3:

		ask_word = str(input('Enter a word : '))

		empty.append(ask_word)

		check_word = [word_tokenize(word) for word in empty]

		time += 1


def find_lexical_diff():

	global time
	time = 2
	global lex
	lex = []
	limit = 0
	pick_rule = ['text1','text2',
				'text3','text4',
				'text5','text6',
				'text7','text8',
				'text9']

	while limit < time:

		try:
			pick_text = str(input('Pick a text : '))

			if pick_text in pick_rule:
				lex.append(pick_text)
				limit += 1
			else:
				system_clean()
				pass
		except NameError:
			break

	print(lex)

find_lexical_diff()
def print_texts():
	print(texts())

def print_sents():
	print(sents())

def ask_text_sent():

	ask_1 = str(input('Do you want to display Text? : '))
	ask_2 = str(input('Do you want to display Sent? : '))

	if ask_1 == 'y'.lower() and ask_2 == 'y'.lower():
		system_clean()
		print_texts()
		print_sents()
	elif ask_1 == 'y'.lower() and ask_2 == 'n'.lower() :
		system_clean()
		print_texts()
	elif ask_2 == 'y'.lower() and ask_1 == 'n'.lower():
		system_clean()
		print_sents()
	else:
		system_clean()
		raise SystemExit

def random_text():

	t1 = random.randint(1,26)
	num_letter_order = []

	y = list(string.ascii_lowercase[:26])

	z = y[t1]

	return z

def plot_lexical_comparison():

	ask_three.dispersion_plot([])

tokenizer()
print(empty)


