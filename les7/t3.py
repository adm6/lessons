users = [{'ismi': 'Olim',
          'login': 'olim4',
          'parol': 'milo'}, {'ismi': 'Jasur',
                             'login': 'jasur2',
                             'parol': 'rusaj'}, {'ismi': 'Javlon',
                                                 'login': 'javlon90',
                                                 'parol': 'nolvaj'}]

login = input('Login: ')
parol = input('Parol: ')

for user in users:
    if login == user['login'] and parol == user['parol']:
        print('Salom ', user['ismi'], '!')
