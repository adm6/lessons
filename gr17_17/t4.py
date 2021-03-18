def find_operator(number):
    code = {33: 'Humans',
            71: 'TashTT',
            93: 'Ucell',
            94: 'Ucell',
            88: 'Mobiuz',
            97: 'Mobiuz',
            90: 'Beeline',
            91: 'Beeline'}
    return code[int(str(number)[3:5])]


li = [998901202020, 998335677789, 998903588383, 998710000000]

for num in li:
    print(find_operator(num))