def get_number():
    while True:
        x = input('Iltimos, raqam kiriting: ')
        if x.isdigit():
            return int(x)


print(get_number())
