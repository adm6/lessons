x = int(input('son kiriting: '))
x_tub_sonmi = True
for i in range(2, x):
    if x % i == 0:
        x_tub_sonmi = False

if x_tub_sonmi:
    print('x tub son')
else:
    print('x tub son emas')