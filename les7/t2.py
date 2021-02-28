txt = input('Satr kiriting: ')
dic = {}
li = []
top_value = [0, 0, 0]

for i in txt:
    dic[i] = txt.count(i)

li = list(dic.values())

top_value[0] = li.pop(li.index(max(li)))
top_value[1] = li.pop(li.index(max(li)))
top_value[2] = li.pop(li.index(max(li)))

dic.clear()
for i in txt:
    element_soni = txt.count(i)
    if element_soni in top_value:
        dic[i] = element_soni

print(dic)
