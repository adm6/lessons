raqamlar = []
satrlar = []
qiymat = input('Istalgan malumotni kiriting: ')

while len(qiymat) > 0:
    if qiymat.isdigit():
        raqamlar.append(qiymat)
    else:
        satrlar.append(qiymat)
    qiymat = input('Keyingi malumotni kiriting: ')

print('Kiritish tugallandi!')
print('Raqamlar: ', raqamlar)
print('Satrlar: ', satrlar)
