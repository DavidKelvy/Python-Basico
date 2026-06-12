# Exemplo 1: JSON para dicionário
import json
json_texto = '{"nome": "João", "cidade": "São Paulo"}'
usuario = json.loads(json_texto)
print(usuario['nome'])

# Exemplo 2: Dicionário para JSON
dados = {'nome': 'Mariana', 'idade': 29}
json_texto = json.dumps(dados, ensure_ascii=False)
print(json_texto)

# Exemplo 3: Resposta de API simulada
resposta = {
    'status': 'ok',
    'dados': [
        {'id': 1, 'valor': 100},
        {'id': 2, 'valor': 200},
    ]
}
for item in resposta['dados']:
    print(item['id'], item['valor'])
