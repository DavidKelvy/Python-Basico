"""Capítulo 06: Dicionários e coleções
Este arquivo mostra como usar dicionários e listas juntos.
"""

usuario = {'nome': 'Ana', 'idade': 22, 'cidade': 'Recife'}
print(usuario['nome'])
usuario['email'] = 'ana@example.com'
for chave, valor in usuario.items():
    print(f'{chave}: {valor}')

usuarios = [
    {'nome': 'Bia', 'idade': 20},
    {'nome': 'Caio', 'idade': 25},
]
for pessoa in usuarios:
    print(pessoa['nome'], 'tem', pessoa['idade'], 'anos')

if usuarios[0]['idade'] > 18:
    print(usuarios[0]['nome'], 'é maior de idade')
