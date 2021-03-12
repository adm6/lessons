li = []

for i in range(25):
    li.append('')
    for j in range(i+1):
        li[i] = str(li[i]) + str(j)

print(li)