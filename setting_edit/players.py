import json

player_refer = ['number', 'name', 'place', 'money', 'own[]', 'moved']
player_1 = [1, 'Alex', 0, 1500, [0], False]
player_2 = [2, 'Bob', 0, 1500, [0], False]
player_3 = [3, 'Calvin', 0, 1500, [0], False]
player_4 = [4, 'Derek', 0, 1500, [0], False]

players = [player_refer, player_1, player_2, player_3, player_4]

# Save data
with open('../settings/players.txt', 'w') as filehander:
    json.dump(players, filehander)
