num = int(input('Son kiriting: '))
num_tub = True

for i in range(2, num):
    if num % i == 0:
        num_tub = False
        break

if num_tub:
    print('Siz kiritgan sonning ozi tub son')
else:
    num_up = num + 1
    num_down = num - 1
    while True:
        tub = True
        for i in range(2, num_up):
            if num_up % i == 0:
                tub = False
        if tub:
            print(num_up)
            break

        tub = True
        for i in range(2, num_down):
            if num_down % i == 0:
                tub = False
        if tub:
            print(num_down)
            break

        num_up = num_up + 1
        num_down = num_down - 1