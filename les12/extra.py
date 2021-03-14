def exchange(currency1, currency2, value):
    exchange_course = {
        'dollar': {'som': 10519, 'rubl': 73.26},
        'rubl': {'som': 143, 'dollar': 0.014},
        'som': {'dollar': 0.000095, 'rubl': 0.01}
    }
    return exchange_course[currency1][currency2] * value

while True:
    hint = "Qaysi valyutadan qaysi valyutaga va summani probel bilan kiriting.\nMasalan: 'dollar som 100': "
    lis = input(hint).split()
    print(exchange(lis[0], lis[1], int(lis[2])))
