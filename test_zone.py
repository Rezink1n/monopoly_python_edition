
x = ''

player_refer = ['name', 'place', 'money', 'own[]', 'moved']
player_1 = ['Ruslan', 0, 1500, [0]]
player_2 = ['Alex', 0, 1500, [0]]

players = [player_refer, player_1, player_2]

def buy_card(player, place, file):
    place_finder(place)
    a = input('Do you want to buy it?\n >')
    if a == 'y':
        players[player][2] -= file[place_finder(place)[0]][3]
        print('You buy it! Congrats!')
        print('Money:', player_1[2])
        player_1[3].append(file[place_finder(place)[0]][0])
    elif a == 'n':
        print('You did not buy it :(')
    elif a == 's':
        print('You have:', player_1[3])
    return print('Next move!')

# Checking list
# def checking_list(loaded_file, file_name):
#     y = 1
#     while y < len(json_reader(file_name)):
#         x = loaded_file[y]
#         i = 0
#         while i < len(loaded_file[0]):
#             print(loaded_file[0][i], end=' - ')
#             print(x[i])
#             i += 1
#         i = 0
#         print('\n')
#         y += 1

# while x != 0:
#     x = int(input('Place: '))
#     buy_card(0, x)

# def save_list(list):
#     import json
#     with open('settings/building.txt', 'w') as filehander:
#         json.dump(list, filehander)

# Read json file
# def json_reader(file_path):
#     with open(file_path, 'r') as filehander:
#         import json
#         loaded_file = json.load(filehander)
#     print(loaded_file)  # Test JSON reading
#     print('json_reader complete')
#     return loaded_file


# def moving_list(list_from):
#     y = 0
#     list_done = []
#     while y < len(list_from):
#         place = list_from[y][0]
#         name = list_from[y][2]
#         cost = list_from[y][3]
#         owner = list_from[y][4]
#         bail_cost = list_from[y][8]
#         bailed = list_from[y][9]
#         group = list_from[y][1]
#         rent = list_from[y][5]
#         houses = list_from[y][6]
#         house_cost = list_from[y][7]
#         monopolized = list_from[y][10]
#
#         list_to = [place, name, owner, cost, bail_cost, bailed, group, rent, houses, house_cost, monopolized]
#         list_done.append(list_to)
#         # print(list_to) # Test work
#         y += 1
#     #print(list_done)
#     return list_done








