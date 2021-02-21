a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))

for i in range(a+1, b):
    for j in range(a+1, b):
        if i + j == b:
            print('b = ', i, ' + ', j)