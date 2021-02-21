n = int(input('n ni kiriting: '))

for i in range(n):
    sum = 0

    for j in range(i):
        sum = sum + j

    print(i, ':  ', sum)
