
x = ''

player_refer = ['name', 'place', 'money', 'own[]']
player_1 = ['Ruslan', 0, 1500, [0]]


def buy_card(player, place):
    place_finder(place)
    print('Money:', player_1[2])
    a = input('Do you want to buy it?\n >')
    if a == 'yes':
        player_1[2] -= cards_json[place_finder(place)[0]][3]
        print('You buy it! Congrats!')
        print('Money:', player_1[2])
        player_1[3].append(cards_json[place_finder(place)[0]][0])
    elif a == 'no':
        print('You did not buy it :(')
    elif a == 'show':
        print('You have:', player_1[3])
    return print('Next move!')


def place_finder(place):
    i = 0
    f = 0
    while i < len(cards_json):
        if cards_json[i][0] == place:
            break
        else:
            i += 1
            f += 1
    return i, print(cards_json[i])


place = 10
card_current = place_finder(place)

print(card_current)

# while x != 0:
#     x = int(input('Place: '))
#     buy_card(0, x)



