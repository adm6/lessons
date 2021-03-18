i = 9999999
while True:
    i = i + 1
    tub_son = True
    for k in range(2, i):
        if i % k == 0:
            tub_son = False

    if tub_son:
        print(i)