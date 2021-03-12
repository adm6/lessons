x = 5
y = 0.25
b = True

with open('t1.txt', 'w') as file:
    file.write('x ' + str(x) + '\n')
    file.write('y ' + str(y) + '\n')
    file.write('b ' + str(b) + '\n')