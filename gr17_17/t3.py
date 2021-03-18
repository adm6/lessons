def get_info():
    return {'name': input('Ismingiz: '),
            'adres': input('Adresingiz: '),
            'number': input('Tel.: ')}


info = get_info()
print(info)