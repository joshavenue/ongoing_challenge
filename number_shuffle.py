from math import floor
import random

count = 0;
a = '1 2 3'.split()
b = '3 2 1'.split()

def shuffler(x,y):
    random.shuffle(x)
    random.shuffle(y)

def compare_deck(x,y):
    if x == y:
        return False
    else:
        return True

while True:
    shuffler(a,b)
    compare_deck(a,b)
    count += 1
    continue

else:
    print('It took {} times of shuffle to be the same arrangement.'.format(count))
    
