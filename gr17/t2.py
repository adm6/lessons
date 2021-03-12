tub_sonlar = []

for i in range(1, 1000):
    son_tub = True
    for j in range(2, i):
        if i % j == 0:
            son_tub = False

    if son_tub:
        tub_sonlar.append(i)

print(tub_sonlar[-1], tub_sonlar[-2])