"""Capítulo 17: Dados de API e JSON
Este arquivo mostra como trabalhar com dicionários e dados de API simulados.
"""

resposta = {
    'nome': 'Python',
    'descricao': 'Linguagem de programação',
    'estrelas': 150000,
}
print('Nome:', resposta['nome'])
print('Estrelas:', resposta['estrelas'])
for chave, valor in resposta.items():
    print(f'{chave}: {valor}')
