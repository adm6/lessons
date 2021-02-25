n = int(input('Raqam kiriting: '))
kiritilgan_raqamlar = []

while n != 0:
    kiritilgan_raqamlar.append(n)
    n = int(input('Keyingi raqamni kiriting: '))

print('0 kiritildi.')
print('kiritilgan raqamlar: ', kiritilgan_raqamlar)
