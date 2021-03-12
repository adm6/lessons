my_variables = {}
with open('t3.txt', 'r') as file:
    for line in file.readlines():
        var_list = line.split(' ')
        my_variables[var_list[0]] = var_list[1].replace('\n', '')

# print(my_variables)
login = input('Loginni kiriting: ')
password = input('Parolni kiriting: ')
if my_variables['login'] == login and my_variables['password'] == password:
    print(f"Salom {my_variables['name']}!")