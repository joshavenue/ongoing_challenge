from datetime import datetime
day_now = datetime.now()

print('Let\'s recruit people by age')
print('Today is {} / {} / {}'.format(day_now.day,day_now.month,day_now.year))

i = 0;
num_data = [1,2,3,4,5,6,7,8,9,0]
alphabet = ['abcdefghijklmnopqrdtuvwxyz']
boolean_yes = ['y']
boolean_no = ['n']
name = []
age = []

def get_help():
    print('Type \'END\' when you are done.')
    print('Type \'ERASE\' when you want to choose again.')
    print('Type \'HELP\' when you need help.')
    print('Type \'SHOW\' when you need to check your list.')
    print('Type \'EXIT\' to stop the program.')
def clean_up_name():
    del name[:]

def clean_up_age():
    del age[:]

def erase_All():
    del name[:]
    del age[:]

def show_list_END():
    print('You have recruited {} people today.'.format(len(name)))
    for names in name and ages in age :
        print(names, ' - ',ages)

def show_list():
    for names in name and ages in age :
        print(names, ' - ',ages)

def warning():
    if name[len(name)] in num_data:
        print('Number is not allow in naming')
    else:
        pass

while True:
    print('You have {} new recruits.'.format(len(name)))
    new_name = input('NAME : ')
    new_age = input('AGE :')
    
    
    if new_name.lower() == 'DONE'.lower() or new_age.lower() == 'DONE'.lower():
        break
    elif new_name.lower() == 'CLEAN'.lower() or new_age.lower == 'CLEAN':
        erase_All()
        continue

    elif new_name.lower() == "HELP".lower() or new_age.lower() == 'HELP'.lower():
        get_help()
        continue
    elif new_name.lower() == 'EXIT'.lower():
        raise SystemExit

    elif new_name.lower() == 'SHOW'.lower() or new_age.lower() == 'SHOW'.lower():
        show_list()
        continue
    else:
        name.append(new_name)
        age.append(new_age)

show_list_END()
