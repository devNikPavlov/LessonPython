# Создание сегмента

players = [
    'charles',
    'martina',
    'michael',
    'florance',
    'eli'
]

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

# Перебор содержимого сегмента
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())





