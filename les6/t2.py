number = int(input('Raqam kiriting: '))
total = 0

while total < 100:
    print('Kiritilgan raqamlar umumiy yigindisi: ', total)
    number = int(input('Keyingi raqamni kiriting: '))
    total += number

print('Kiritilgan raqamlar yigindisi 100 dan oshdi!')
