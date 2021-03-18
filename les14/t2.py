def write_contact(name, number):
    with open('contacts.txt', 'a') as contacts:
        contacts.write(f'{name}={number}\n')


def get_contact_list():
    contacts = {}
    with open('contacts.txt', 'r') as file:
        lines = [c.replace('\n', '').split('=') for c in file.readlines()]

    for k, v in lines:
        contacts[k] = v
    return contacts


def get_contact(name):
    contacts = get_contact_list()
    if name in contacts:
        return contacts[name]
    return 'Kontakt topilmadi.'


while True:
    tanlov = input('1. Kontakt qoshish.  2. Kontaktni topish.\nTanlang 1 yoki 2: ')
    if tanlov == '1':
        ismi = input('Ismini kiriting: ')
        nomeri = input('Nomerini kiriting: ')
        write_contact(ismi, nomeri)
        print('Kontakt saqlandi')
    elif tanlov == '2':
        ismi = input('Ismini kiriting: ')
        print(get_contact(ismi))
