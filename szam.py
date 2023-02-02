
import random

def gen_szam():

    vel = random.randint(1,50)
    print('I/A:')
    print(f'\tA generált szám: {vel}')
    print('I/B:')
    if vel % 5 == 0 and vel % 3 == 0:
        print(f'\tA szám öttel és hárommal is osztható!')
    elif vel % 5 == 0:
        print(f'\tA szám öttel osztható!')
    elif vel % 3 == 0:
        print(f'\tA szám hárommal osztható!')