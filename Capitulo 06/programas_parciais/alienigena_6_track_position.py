alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Posição original: {alien_0['x_position']}")

# Mova o alienígena para a direita.
# Determine o quanto mover o alienígena com base em sua velocidade atual.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienígena rápido.
    x_increment = 3

# A nova posição é a posição antiga mais o incremento.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Nova posição: {alien_0['x_position']}")