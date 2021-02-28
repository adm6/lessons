user = {'ismi': input('Ismingiz: '),
        'familiyasi': input('Familiyangiz: '),
        'yoshi': input('Yoshingiz: '),
        'kasbi': input('Kasbingiz: '),
        'manzil': input('Yashash manzilingiz: '),
        'tel': input('Telefon raqamingiz: ')}

# print(user)

for k, v in user.items():
    print(k, ':  ', v)
