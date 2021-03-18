fib_list = [0, 1]
result = []

while len(result) < 10:
    fib_list.append(fib_list[-2] + fib_list[-1])

    tub_son = True
    n = fib_list[-1]
    for i in range(2, n):
        if n % i == 0:
            tub_son = False

    if tub_son:
        result.append(n)


print(result)