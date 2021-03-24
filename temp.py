try:
    with open('test.txt', 'w') as file:
        print(file.readlines())
except Exception:
    print('go')