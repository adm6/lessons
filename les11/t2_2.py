with open('t2.txt', 'r') as file:
    line = file.readline().strip()
    fib_list = line.split(' ')

print(type(fib_list))
print(fib_list)
for i in range(len(fib_list)):
    fib_list[i] = int(fib_list[i])
print(fib_list)