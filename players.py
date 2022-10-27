import json

player_refer = ['name', 'place', 'money', 'own[]']
player_1 = ['Ruslan', 0, 1500, [0]]
player_2 = ['Alex', 0, 1500, [0]]

players = [player_refer, player_1, player_2]

# Save data
with open('players/players.txt', 'w') as filehander:
    json.dump(players, filehander)
