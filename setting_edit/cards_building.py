import json


card_refer = ['place', 'group', 'name', 'cost', 'owner',
              'rent', 'buildings', 'build_cost',
              'bail_cost', 'bailed', 'monopolized']

# Orange
card_1 = [1, 'orange', 'Old Road', 60, 'free',
          [2, 10, 30, 90, 160, 250], 0, 50,
          30, False, False]

card_2 = [3, 'orange', 'Highway', 60, 'free',
          [4, 20, 60, 180, 320, 450], 0, 50,
          30, False, False]

# Yellow
card_3 = [6, 'yellow', 'Waterpark', 100, 'free',
          [6, 30, 90, 270, 400, 550], 0, 50,
          50, False, False]

card_4 = [8, 'yellow', 'City Park', 100, 'free',
          [6, 30, 90, 270, 400, 550], 0, 50,
          50, False, False]

card_5 = [9, 'yellow', 'Ski Resort', 120, 'free',
          [8, 40, 100, 300, 450, 600], 0, 50,
          60, False, False]

# Green
card_6 = [11, 'green', 'Спальный район', 140, 'free',
          [10, 50, 150, 450, 625, 750], 0, 100,
          70, False, False]
card_7 = [13, 'green', 'Деловой квартал', 140, 'free',
          [10, 50, 150, 450, 625, 750], 0, 100,
          70, False, False]
card_8 = [14, 'green', 'Торговая площадь', 160, 'free',
          [12, 60, 180, 500, 700, 900], 0, 100,
          80, False, False]

# Lime
card_9 = [16, 'lime', 'Улица Пушкина', 180, 'free',
          [14, 70, 200, 550, 750, 950], 0, 100,
          90, False, False]
card_10 = [18, 'lime', 'Проспект Мира', 180, 'free',
           [14, 70, 200, 550, 750, 950], 0, 100,
           90, False, False]
card_11 = [19, 'lime', 'Проспект Победы', 200, 'free',
           [16, 80, 220, 600, 800, 1000], 0, 100,
           100, False, False]

# Brown
card_12 = [21, 'brown', 'Бар', 220, 'free',
           [18, 90, 250, 700, 875, 1050], 0, 150,
           110, False, False]
card_13 = [23, 'brown', 'Ночной клуб', 220, 'free',
           [18, 90, 250, 700, 875, 1050], 0, 150,
           110, False, False]
card_14 = [24, 'brown', 'Ресторан', 240, 'free',
           [20, 10, 300, 750, 925, 1100], 0, 150,
           120, False, False]

# Purple
card_15 = [26, 'purple', 'Компьютеры', 260, 'free',
           [22, 110, 330, 800, 975, 1150], 0, 150,
           130, False, False]
card_16 = [27, 'purple', 'Интернет', 260, 'free',
           [22, 110, 330, 800, 975, 1150], 0, 150,
           130, False, False]
card_17 = [29, 'purple', 'Сотовая связь', 280, 'free',
           [24, 120, 360, 850, 1025, 1200], 0, 150,
           140, False, False]

# Sea
card_18 = [31, 'sea', 'Морские перевозки', 300, 'free',
           [26, 130, 390, 900, 1100, 1275], 0, 200,
           150, False, False]
card_19 = [32, 'sea', 'Железная дорога', 300, 'free',
           [26, 130, 390, 900, 1100, 1275], 0, 200,
           150, False, False]
card_20 = [34, 'sea', 'Авиакомпания', 320, 'free',
           [28, 150, 450, 1000, 1200, 1400], 0, 200,
           160, False, False]

# Blue
card_21 = [37, 'blue', 'Курортная зона', 350, 'free',
           [35, 175, 500, 1100, 1300, 1500], 0, 200,
           175, False, False]
card_22 = [39, 'blue', 'Гостиничный комплекс', 400, 'free',
           [50, 200, 600, 1400, 1700, 2000], 0, 200,
           200, False, False]

cards_building = [card_refer, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11,
                  card_12, card_13, card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22]

# Save data
with open('../cards/cards_building.txt', 'w') as filehander:
    json.dump(cards_building, filehander)

print(cards_building)
print('Data is saved')
