import random

from cards_building import cards_building
from players import players


def make_step(place):
    d = random.randint(2, 12)
    place += d
    if place > 39:
        place -= 40
        money_up(1, 200)
    return place, d


def place_type_is(place):
    match place:
        case 0: place_type = 'Start'
        case 4: place_type = 'Taxes'
        case 10: place_type = 'Prison'
        case 12 | 28: place_type = 'Company'
        case 20: place_type = 'Free parking'
        case 30:
            place_type = 'Arrest'
            new_place(1, 10)
        case 38:
            place_type = '-100$'
            money_down(1, 100)
        case 5 | 15 | 25 | 35: place_type = 'Seaport'
        case 2 | 17 | 33: place_type = 'Treasury'
        case 7 | 22 | 36: place_type = 'Chance'
        case _:
            place_type = 'Building'
            check_building(players[1][1], cards_building)
    return place_type


def building_finder(place, file):
    for i in range(len(file)):
        if file[i][0] == place:
            break
    return file[i]


def money_up(player, quantity):
    players[player][2] += quantity


def money_down(player, quantity):
    players[player][2] -= quantity


def new_place(player, place):
    players[player][1] = place


def check_building(place, file):
    b = building_finder(place, file)
    if b[4] == 'free':
        print('Free', end=' ')
    else:
        print('Owner:', b[4])

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




def buy_building(player, place, file):
    return
