import json


seaport_refer = ['place', 'seaport', 'name', 'cost', 'owner',
              'rent', 'quantity', 'build_cost',
              'bail_cost', 'bailed', 'monopolized']

seaport_1 = [5, 'seaports', 'West seaport', 200, 'free',
              [25, 50, 100, 200], 0, 'null',
              100, False, 'null']

seaport_2 = [15, 'seaports', 'North seaport', 200, 'free',
              [25, 50, 100, 200], 0, 'null',
              100, False, 'null']

seaport_3 = [25, 'seaports', 'East seaport', 200, 'free',
              [25, 50, 100, 200], 0, 'null',
              100, False, 'null']

seaport_4 = [35, 'seaports', 'South seaport', 200, 'free',
              [25, 50, 100, 200], 0, 'null',
              100, False, 'null']

cards_seaport = [seaport_refer, seaport_1, seaport_2, seaport_3, seaport_4]

print(cards_seaport)

# Save data
with open('cards/cards_seaport.txt', 'w') as filehander:
    json.dump(cards_seaport, filehander)

print('Data is saved')