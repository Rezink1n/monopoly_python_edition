#  ADD GitHub
import functions_all as func
from players import players
from cards_building import cards_building


act = ''
place = players[1][1]
money = players[1][2]

while act != exit:
    act = input(' > ')
    match act:
        case 'info': print('Info')
        case 'move':
            place, dice = func.make_step(place)
            print('Dice:', dice, '\nPlace:', place)
            print(func.place_type_is(place), end='|')
            print('Money:', money)
        case 'exit':
            print('Exit')
            break
