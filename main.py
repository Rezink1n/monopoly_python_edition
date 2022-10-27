#  ADD GitHub
import functions_all as func
from players import players
from cards_building import cards_building



for i in range(100):
    players[1][1], dice = func.make_step(players[1][1])

    print('+', dice, players[1][1], end='|')
    print(func.place_type_is(players[1][1]), end='|')
    print('Money:', players[1][2])


