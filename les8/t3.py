def unlilar_soni(txt):
    unlilar = ['a', 'e', 'i', 'o', 'u']
    unlilar_soni = 0

    for i in txt:
        if i in unlilar:
            unlilar_soni = unlilar_soni + 1

    return unlilar_soni


satr = input('Satr kiriting: ')
print(unlilar_soni(satr))
