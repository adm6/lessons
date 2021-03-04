import random


fib_list = [0, 1]

while (fib_list[-2] + fib_list[-1]) < 5000:
    fib_list.append(fib_list[-1] + fib_list[-2])

for i in range(3):
    print(fib_list[random.randint(0, len(fib_list)-1)])