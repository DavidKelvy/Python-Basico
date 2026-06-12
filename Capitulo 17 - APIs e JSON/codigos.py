import json

texto = '{"nome": "Ana", "idade": 30, "habilidades": ["Python", "SQL"]}'
dados = json.loads(texto)

dados['cidade'] = 'Porto Alegre'
dados['idade'] += 1

saida_texto = json.dumps(dados, ensure_ascii=False, indent=2)
print('Dados em Python:', dados)
print('JSON formatado:')
print(saida_texto)

# Simulando uma resposta de API com lista de itens
resposta = {
    'status': 'ok',
    'dados': [
        {'id': 1, 'nome': 'Produto A', 'preco': 19.9},
        {'id': 2, 'nome': 'Produto B', 'preco': 29.9},
    ]
}
json_api = json.dumps(resposta, ensure_ascii=False)
print('Resposta API JSON:', json_api)
print('Nome do primeiro item:', resposta['dados'][0]['nome'])
