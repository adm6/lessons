satr = input('Satr kiriting: ')
numbers = 0

for i in satr:
    if i.isdigit():
        numbers += 1

print('Kiritilgan satrdagi raqamlar soni: ', numbers)