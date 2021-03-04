import time


names = {'soat': 'H',
         'minut': 'M',
         'sekund': 'S'}

while True:
    name = input('soat, minut yoki sekund deb yozing: ')
    if name in names:
        print(time.strftime(f"%{names[name]}"))
    else:
        print('Iltimos aniq va to\'g\'ri yozing!')