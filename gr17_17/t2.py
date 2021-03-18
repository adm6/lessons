def get_max_sum(list_1, list_2, list_3):
    sum1, sum2, sum3 = sum(list_1), sum(list_2), sum(list_3)
    if sum1 > sum2 and sum1 > sum3:
        return list_1
    elif sum2 > sum1 and sum2 > sum3:
        return list_2
    else:
        return list_3


l1 = [1, 2, 3]
l2 = [2, 4, 5]
l3 = [8, 3, 7]

print(get_max_sum(l1, l2, l3))