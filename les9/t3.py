import random


result = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for i in range(1000):
    x = random.randint(0, 9)
    s = str(x)
    result[s] = result[s] + 1

print(result)