def unique_elements(li):
    new_li = []
    for i in li:
        if li.count(i) == 1:
            new_li.append(i)

    return new_li


print(unique_elements(['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c']))