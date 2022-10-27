import random


def place_finder(place, file):
    i = 0
    f = 0
    while i < len(file):
        if file[i][0] == place:
            break
        else:
            i += 1
            f += 1
    return i, print(file[i])


def make_step(place):
    d = random.randint(2, 12)
    place += d
    if place > 39:
        place -= 40
    return place, d


def money_up(player, quantity):
    players[player][2] += quantity


def money_down(player, quantity):
    players[player][2] -= quantity
