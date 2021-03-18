def is_uzb_number(number):
    number = str(number)
    return number.startswith('998') and len(number) == 12



numbers = [198901202020, 998335677789, 994903588383, 998710000000, 9983311122334]

for num in numbers:
    print(is_uzb_number(num))