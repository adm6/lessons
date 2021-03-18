def get_top_3(li):
    return [li.pop(li.index(max(li))), li.pop(li.index(max(li))), li.pop(li.index(max(li)))]


lis = [0, 8, 9, 7, 5, 4, 3, 2, 1]
print(get_top_3(lis))
