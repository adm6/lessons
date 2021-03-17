def ulilar_sone(txt):
    u_soni = 0
    unlilar = ['a', 'e', 'i', 'o', 'u']
    for i in txt:
        if i in unlilar:
            u_soni += 1

    return u_soni


print(ulilar_sone('bu text tekshirish va unlilarni sonini topish uchun'))