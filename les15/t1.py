def get_elements(list1, list2):
    rezult = []
    [rezult.append(i) for i in list1 if (i in list2 and i not in rezult)]
    return rezult


li1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c']
li2 = ['b', 'd', 'f', 'j', 'w', 'f', 'a', 'c', 'd']

print(get_elements(li1, li2))