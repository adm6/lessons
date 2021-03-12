my_variables = {}
with open('t1.txt', 'r') as file:
    for line in file.readlines():
        var_list = line.split(' ')
        my_variables[var_list[0]] = var_list[1].replace('\n', '')

print(my_variables)
my_variables['x'] = int(my_variables['x']) + 5
my_variables['y'] = float(my_variables['x']) + 1.25
my_variables['b'] = not bool(my_variables['x'])

print(my_variables)