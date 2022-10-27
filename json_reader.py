import json

# Read data

file_name = 'cards/cards_building.txt'


def json_reader(file_name):
    with open(file_name, 'r') as filehander:
        file = json.load(filehander)
    print(file)  # Test JSON reading
    print('json_reader complete')
    return file



# Checking list
def checking_list(file):
    i2 = 1
    while i2 < len(file):
        x = file[i2]
        i = 0
        while i < len(file[0]):
            print(file[0][i], end=' - ')
            print(x[i])
            i += 1
        i = 0
        print('\n')
        i2 += 1


def place_finder(place, file):
    i = 0
    f = 0
    while i < len(file):
        if file[i][0] == place:
            break
        else:
            i += 1
            f += 1
    return print(file[i])


# while x != 0:
#     x = int(input('Введите номер клетки: '))
#
#     place_finder(x)

json_reader(file_name)


