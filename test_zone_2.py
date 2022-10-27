def place_type_is(place):
    match place:
        case 0: place_type = 'Start'
        case 4: place_type = 'Taxes'
        case 10: place_type = 'Prison'
        case 12 | 28: place_type = 'Company'
        case 20: place_type = 'Free parking'
        case 30: place_type = 'Arrest'
        case 38: place_type = '-100$'
        case 5 | 15 | 25 | 35: place_type = 'Seaport'
        case 2 | 17 | 33: place_type = 'Treasury'
        case 7 | 22 | 36: place_type = 'Chance'
        case _: place_type = 'Building'
    return place_type


for i in range(40):
    print(i, place_type_is(i))
