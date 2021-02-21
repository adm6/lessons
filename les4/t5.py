first = 0
second = 1
rezerv = 0

while first < 220:
    print(first)
    rezerv = first + second
    first = second
    second = rezerv
