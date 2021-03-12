name = input('Ismingizni kiriting: ')
login = input('Loginni kiriting: ')
password = input('Parolni kiriting: ')

with open('t3.txt', 'w') as file:
    file.write('name ' + str(name) + '\n')
    file.write('login ' + str(login) + '\n')
    file.write('password ' + str(password) + '\n')