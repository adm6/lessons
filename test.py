import time
import datetime
import random


x = random.randint(0, 100)
started_time = datetime.datetime.now()
jon = 4

while True:
    if jon < 1:
        print('Joningiz tugadi!')
        break
    next_time = datetime.datetime.now()
    entered_num = int(input('\nx ni toping: '))
    if entered_num > x:
        print('kichikroq...')
    elif entered_num < x:
        print('kattaroq...')
    else:
        print('Topdingiz!')
        break

    jon = jon - 1

    delta = datetime.datetime.now() - next_time
    print('oxirgi urunish uchun ketgan vaqt: ', delta.seconds)
    delta = datetime.datetime.now() - started_time
    print('oyin boshlanganidan beri otgan vaqt: ', delta.seconds)
    print('jon = ', jon)


delta = datetime.datetime.now() - started_time
print('umumiy vaqt: ', delta.seconds)