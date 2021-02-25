txt = input('Satr kiriting: ')
printed = []

for i in txt:
    if (txt.count(i) > 1) and (i not in printed):
        print(i)
        printed.append(i)








# txt = input('Satr kiriting: ')
# one = list(set(txt))
# for i in one:
#     if txt.count(i) > 1:
#         print(i)
