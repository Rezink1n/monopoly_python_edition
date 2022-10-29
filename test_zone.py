# def buy_card(player, place, file):
#     place_finder(place)
#     a = input('Do you want to buy it?\n >')
#     if a == 'y':
#         players[player][2] -= file[place_finder(place)[0]][3]
#         print('You buy it! Congrats!')
#         print('Money:', player_1[2])
#         player_1[3].append(file[place_finder(place)[0]][0])
#     elif a == 'n':
#         print('You did not buy it :(')
#     elif a == 's':
#         print('You have:', player_1[3])
#     return print('Next move!')

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








