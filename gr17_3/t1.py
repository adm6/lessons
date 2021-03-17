def tub_sonlar(a, b):
    for i in range(a, b):
        tub_son = True
        for j in range(2, i):
            if i % j == 0:
                tub_son = False
        if tub_son:
            print(i)


tub_sonlar(3, 20)