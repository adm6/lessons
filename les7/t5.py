dic = {}

for i in range(1, 25):
    dic[i] = 0
    for k in range(i):
        dic[i] = dic[i] + k

print(dic)
