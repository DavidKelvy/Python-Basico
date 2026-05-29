"""Capítulo 06: Dicionários e coleções de dados
Este complemento apresenta como usar dicionários e listas de forma conjunta.
"""

# Criar dicionário de usuário
usuario = {'nome': 'lucas', 'idade': 25, 'cidade': 'São Paulo'}
print(usuario['nome'])

# Adicionar e atualizar valores
usuario['email'] = 'lucas@example.com'
usuario['idade'] = 26

# Percorrer dicionário
for chave, valor in usuario.items():
    print(f'{chave}: {valor}')

# Lista de dicionários
usuarios = [
    {'nome': 'ana', 'idade': 22},
    {'nome': 'bia', 'idade': 28},
    {'nome': 'caio', 'idade': 31},
]
for pessoa in usuarios:
    print(pessoa['nome'], 'tem', pessoa['idade'], 'anos')

# Usar valores em condições
if usuarios[0]['idade'] > 18:
    print(usuarios[0]['nome'], 'é maior de idade')
