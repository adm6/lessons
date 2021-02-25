txt = input('Satr kiriting: ')
li = []

for i in txt:
    if i not in li:
        li.append(i)

print('Satrda bor elementlar listi: ', li)