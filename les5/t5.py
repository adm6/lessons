entered_num = int(input('Raqam kiriting: '))
raqamlar = []

while entered_num != 0:
    raqamlar.append(entered_num)
    entered_num = int(input('Keyingi raqamni kiriting: '))

print('0 raqami kiritildi va raqam kiritish tugallandi.')

print('Kiritilgan eng katta raqam: ', max(raqamlar))
print('Kiritilgan eng kichik raqam: ', min(raqamlar))
print('Kiritilgan raqamlar o\'rta arifmetik qiymati: ', sum(raqamlar)/len(raqamlar))

