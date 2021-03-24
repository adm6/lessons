def get_ekub(num1, num2):
    for i in range(num1-1, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 0


print(get_ekub(36, 27))