import json


seaport_refer = ["place", "name", "owner", "cost", "bail_cost", "bailed", "rent", "connection"]

seaport_1 = [5, 'West seaport', 'free', 200, 100,
              False, [25, 50, 100, 200], 0]

seaport_2 = [15, 'North seaport', 'free', 200, 100,
              False, [25, 50, 100, 200], 0]

seaport_3 = [25, 'East seaport', 'free', 200, 100,
              False, [25, 50, 100, 200], 0]

seaport_4 = [35, 'South seaport', 'free', 200, 100,
              False, [25, 50, 100, 200], 0]

cards_seaport = [seaport_refer, seaport_1, seaport_2, seaport_3, seaport_4]

print(cards_seaport)

# Save data
with open('../settings/seaport.txt', 'w') as filehander:
    json.dump(cards_seaport, filehander)

print('Data is saved')