fib_list = [0, 1]

while fib_list[-1] < 5000:
    fib_list.append(fib_list[-1] + fib_list[-2])

with open('t2.txt', 'w') as file:
    for i in fib_list:
        file.write(str(i) + ' ')