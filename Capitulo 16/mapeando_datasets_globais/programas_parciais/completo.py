"""Capítulo 16: Mapeando dados globais
Este complemento mostra como preparar dados de localização e magnitudes.
"""

terremotos = [
    {'lugar': 'Chile', 'magnitude': 6.9, 'latitude': -35.4, 'longitude': -71.6},
    {'lugar': 'Japão', 'magnitude': 7.2, 'latitude': 38.3, 'longitude': 142.4},
]

for terremoto in terremotos:
    print(f"{terremoto['lugar']} - magnitude {terremoto['magnitude']}")

mapa = [(t['longitude'], t['latitude'], t['magnitude']) for t in terremotos]
print('Dados do mapa:', mapa)
