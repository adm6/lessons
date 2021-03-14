def is_leap(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    return False


print(is_leap(400))
print(is_leap(300))
print(is_leap(44))
print(is_leap(100))
print(is_leap(1200))