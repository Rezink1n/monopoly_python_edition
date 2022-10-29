import json


seaport_refer = ["place", "name", "owner", "cost", "bail_cost", "bailed", "rent", "connection"]

seaport_1 = [12, 'Energy supply', 'free', 150, 75,
              False, [4, 10], 0]

seaport_2 = [28, 'Water supply', 'free', 200, 100,
              False, [25, 50, 100, 200], 0]


cards_seaport = [seaport_refer, seaport_1, seaport_2]

print(cards_seaport)

# Save data
with open('../settings/company.txt', 'w') as filehander:
    json.dump(cards_seaport, filehander)

print('Data is saved')