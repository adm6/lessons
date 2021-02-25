fib_list = [0]
element = 1

while element < 2000:
    fib_list.append(element)
    element = fib_list[-1] + fib_list[-2]

toq_list = []
juft_list = []

for i in fib_list[1:]:
    if i % 2 == 0:
        juft_list.append(i)
    else:
        toq_list.append(i)

print('toliq list: ', fib_list)
print('juft sonlar: ', juft_list)
print('toq sonlar: ', toq_list)







# first = 0
# second = 1
# rezerv = 0
#
# while first < 220:
#     print(first)
#     rezerv = first + second
#     first = second
#     second = rezerv
