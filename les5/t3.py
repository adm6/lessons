toq_sonlar = []
juft_sonlar = []
entered_number = int(input('Raqam kiriting: '))

while entered_number != 0:
    if entered_number % 2 == 0:
        juft_sonlar.append(entered_number)
    else:
        toq_sonlar.append(entered_number)
    entered_number = int(input('Keyingi raqamni kiriting: '))

print('0 raqami kiritildi.')
print('Toq sonlar: ', toq_sonlar)
print('Juft sonlar: ', juft_sonlar)
