#  ADD GitHub
import functions_all as func


place = 0

# testing
for i in range(20):

    place, dice = func.make_step(place)
    print('Dice:', dice)
    print('Place:', place)
