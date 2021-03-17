def unlilar_soni(txt):
    unlilar = ['a', 'e', 'i', 'o', 'u']
    unli_soni = 0

    for i in txt:
        if i in unlilar:
            unli_soni += 1

    return unli_soni


satr = input('Satr kiriting: ')
print(unlilar_soni(satr))
