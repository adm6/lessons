def tub_sonmi(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return x


def yaqin_tubsonni_top(x):
    step = 1
    result = 0

    while not result:
        if tub_sonmi(x + step):
            result = result + (x + step)
        if tub_sonmi(x - step):
            result = result + (x - step)

        step = step + 1

    return result


print(yaqin_tubsonni_top(6))