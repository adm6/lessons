n = int(input('n ni kiriting: '))

for i in range(1, n):
    if (i % 5 == 0) and (i % 10 != 0):
        print(i)