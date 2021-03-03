def raqam_olish():
    raqam = input('Raqam kiriting: ')

    while not raqam.isdigit():
        raqam = input('Iltimos faqat raqamlardan iborat qiymat kiriting: ')

    return int(raqam)


x = raqam_olish()
x = x + 10
print(x)