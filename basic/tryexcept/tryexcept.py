filename = 'test.txt'

try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    print("Sorry! The file {} cannot found".format(filename))