
x = ''

player_refer = ['name', 'place', 'money', 'own[]']
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

# while x != 0:
#     x = int(input('Place: '))
#     buy_card(0, x)



