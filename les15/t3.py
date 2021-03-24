import random


def find_number():
    x = random.randint(1, 100)
    n = int(input('Random raqamni toping: '))
    while x != n:
        if x < n:
            print('random son kichikroq...')
        elif n < x:
            print('random son kattaroq...')

        n = int(input('Yana urinib koring: '))

    print('Topdingiz!')


find_number()