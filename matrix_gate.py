import numpy as np
import random
import os

try:
    ask_dimension = int(input('How many dimension should a matrix has : '))
    if ask_dimension == 2:
        x = int(input('X-axis dimension : '))
        y = int(input('Y-axis dimension : '))
    elif ask_dimension == 3:
        x = int(input('X-axis dimension : '))
        y = int(input('Y-axis dimension : '))
        z = int(input('Z-axis dimension : '))
    elif ask_dimension == 1:
        print('Nothing but a dot.')
    else:
        print('Invalid dimension.')
        raise SystemExit

except ValueError:
    print('Invalid dimension.')
    raise SystemExit
else:
    pass


if ask_dimension == 2:
    x_origin = int(input('Enter your starting number : '))
    x_end = int(input('Enter your final number : '))
    x_division = int(input('Enter your division power : '))

    if x_origin > x_end:
        print('{} is higher than {}, which is the end point.'.format(x1_origin,x1_end))
        raise SystemExit
    elif x_division > x_end:
        print('This won\'t work.')
        raise SystemExit
    elif x_division > x_origin:
        print('Won\'t work.')
    else:
        pass

    try:
        shape_x = int(input('Enter the x-axis size : '))
        shape_y = int(input('Enter the y-axis size : '))

        if np.size(x*y) < (shape_x * shape_y):
            print('Matrix invalid.')
        elif 
            // Dont know how to do prove matrix prime diviosn //
        else:
            print('Invalid shape dimension.')
            raise SystemExit

    except ValueError:
        print('Invalid shape dimension.')
        raise SystemExit
    
