"""Capítulo 17: Requisições e JSON
Este complemento mostra como trabalhar com dados de requisição e dicionários.
"""

resposta = {
    'nome': 'Python',
    'descrição': 'Uma linguagem de programação',
    'estrelas': 150000,
}

print('Nome:', resposta['nome'])
print('Estrelas:', resposta['estrelas'])

for chave, valor in resposta.items():
    print(f'{chave}: {valor}')
