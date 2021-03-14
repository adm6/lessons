def get_lines(file):
    with open(file, 'r') as reader:
        return reader.readlines()


print(get_lines('../data.txt'))