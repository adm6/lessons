my_dic = {}

for i in range(50):
    my_dic[i] = 0
    for j in range(i):
        my_dic[i] += j

print(my_dic)