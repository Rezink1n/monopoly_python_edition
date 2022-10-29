#  ADD GitHub
import functions as f
import classes


act = ''
player = f.get_player(1)
place = player.place
money = player.money

while act != exit:
    act = input(' > ')
    for i in range(1, 20):
        match act:
            case 'info': print('Info')
            case 'move':
                place, dice = f.make_step(place)
                print('Money:', money)
                print('Dice:', dice, '\nPlace:', place)
                f.place_type_is(place)
                print('=============')
            case 'exit':
                print('Exit')
                break
