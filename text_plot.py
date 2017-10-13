import math
import random
import nltk
import os
from nltk.book import *

selection = [1,2,3,4,5,6,7,8,9]

def system_clean():

	if os.system == 'posix':
		os.system('clr')
	else:
		os.system('clear')

def display_text():

	print(texts())

def check_text(x1,x2,x3):

	if x1.lower() == x1.isalpha():
		pass
	elif x2.lower() == x2.isalpha():
		pass
	elif x3.lower() == x3.isalpha():
		pass
	else
		raise TypeError and SystemExit

def ask_text_sent():

	ask_1 = str(input('Do you want to display Text? : '))
	ask_2 = str(input('Do you want to display Sent? : '))

	return ask_1, ask_2

def find_lexical_diff():

	ask_three = []
	ask_3 = str(input('Which text do you wish to compare?'))

	while len(ask_3) < 3:

		yield ask_3

		if ask_3.lower() not in selection:
			raise LookupError and TypeError
		elif ask_3.lower() in selection:
			ask_three.append(ask_3)
			ask_3 -= 1
			continue
		else:
			break

	return ask_three

def random_text():

	t1 = random.randint(1,26)
	num_letter_order = []

	y = list(string.ascii_lowercase[:26])

	z = y[t1]

	return z

def plot_lexical_comparison():

	ask_three.dispersion_plot([])



