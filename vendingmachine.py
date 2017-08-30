import os

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')
else:
    pass

print('You are planning to do a maintainance on a vending machine.')
vending_machine = []
print('Type \'DONE\' when you are finished.')

while True:
    x = input('What to stock up today? : ')

    vending_machine.append(x)

    if x.lower() == 'done':
        vending_machine.remove('done')
        break
    else:
        pass

while True:
    y = input('What to do remove today? : ')

    vending_machine.remove(y)

    if x.lower() == 'done':
        break
    elif x.lower() not in vending_machine:
        print('It is not in the vending machine.')
    else:
        pass

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')
else:
    pass

print('what is left in the vending machine : {}'.format(vending_machine))
