import random
import classes


def make_step(place):
    d = random.randint(2, 12)
    place += d
    if place > 39:
        place -= 40
        money_up(1, 200)
    return place, d


def place_type_is(place):
    place_type = ''
    match place:
        case 0:
            place_type = 'Start'
        case 4:
            place_type = 'Taxes'
        case 10:
            place_type = 'Prison'
        case 12 | 28:
            place_type = 'Company'
            b = get_company(place)
            b.info()
        case 20:
            place_type = 'Free parking'
        case 30:
            place_type = 'Arrest'
            new_place(1, 10)
        case 38:
            place_type = '-100$'
            money_down(1, 100)
        case 5 | 15 | 25 | 35:
            place_type = 'Seaport'
            b = get_seaport(place)
            b.info()
        case 2 | 17 | 33:
            place_type = 'Treasury'
        case 7 | 22 | 36:
            place_type = 'Chance'
        case _:
            # place_type = 'Building'
            b = get_building(place)
            # check_owner(players[1][1], b.owner)
            b.info()
    print(place_type)


def building_finder(place, file):
    i = 0
    for i in range(len(file)):
        if file[i][0] == place:
            break
    return file[i]


def money_up(player, quantity):
    player.money += quantity


def money_down(player, quantity):
    player.money -= quantity


def new_place(player, place):
    player.place = place


def check_owner(owner):
    if owner == 'free':
        print('Free', end=' ')
    else:
        print('Owner:', owner)


def buy_building(player, place, file):
    return


def get_building(place):
    with open('settings/building.txt', 'r') as filehander:
        import json
        get_json = json.load(filehander)

    for i in range(len(get_json)):
        if get_json[i][0] == place:
            build = classes.Building(get_json[i][0], get_json[i][1], get_json[i][2], get_json[i][3], get_json[i][4],
                                     get_json[i][5], get_json[i][6], get_json[i][7], get_json[i][8], get_json[i][9],
                                     get_json[i][10])
            return build


def get_seaport(place):
    with open('settings/seaport.txt', 'r') as filehander:
        import json
        get_json = json.load(filehander)

    for i in range(len(get_json)):
        if get_json[i][0] == place:
            seaport = classes.Seaport(get_json[i][0], get_json[i][1], get_json[i][2], get_json[i][3],
                                      get_json[i][4], get_json[i][5], get_json[i][6], get_json[i][7])
            return seaport


def get_company(place):
    with open('settings/company.txt', 'r') as filehander:
        import json
        get_json = json.load(filehander)

    for i in range(len(get_json)):
        if get_json[i][0] == place:
            company = classes.Company(get_json[i][0], get_json[i][1], get_json[i][2], get_json[i][3],
                                      get_json[i][4], get_json[i][5], get_json[i][6], get_json[i][7])
            return company


def get_player(number):
    with open('settings/players.txt', 'r') as filehander:
        import json
        get_json = json.load(filehander)

    for i in range(len(get_json)):
        if get_json[i][0] == number:
            player = classes.Player(get_json[i][0], get_json[i][1], get_json[i][2], get_json[i][3],
                                    get_json[i][4], get_json[i][5])
            return player


# -------------------------------------

player = get_player(1)
place = player.place
money = player.money
