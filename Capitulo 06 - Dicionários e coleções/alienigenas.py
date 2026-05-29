# Faça uma lista vazia para armazenar alienígenas.
aliens = []

# Crie 30 alienígenas verdes.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Mostre os primeiros 5 alienígenas.
for alien in aliens[:5]:
    print(alien)
print("...")

# Mostre quantos alienígenas foram criados.
print(f"Número total de alienígenas: {len(aliens)}")