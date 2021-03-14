txt = input('Satr kiriting: ')
summa = 0
for i in txt:
    if i.isdigit():
        summa += int(i)

print(summa)