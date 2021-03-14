while True:
    n = int(input('Raqam kiriting: '))
    if n % 2 == 0:
        print('son juft')
    else:
        print('son toq')
    tub = True
    for i in range(2, n):
        if n % i == 0:
            tub = False

    if tub:
        print('tub son')
    else:
        print('tub son emas')
