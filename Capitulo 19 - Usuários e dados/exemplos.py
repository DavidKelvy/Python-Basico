# Exemplo 1: Lista de usuários
usuarios = [
    {'nome': 'Lucia', 'idade': 35},
    {'nome': 'Pedro', 'idade': 42},
]
print(usuarios)

# Exemplo 2: Adicionar usuário
novo_usuario = {'nome': 'Fernanda', 'idade': 28}
usuarios.append(novo_usuario)
print(usuarios)

# Exemplo 3: Buscar usuário
for usuario in usuarios:
    if usuario['nome'] == 'Pedro':
        print('Encontrado', usuario)

# Exemplo 4: Filtrar maiores de idade
adultos = [u for u in usuarios if u['idade'] >= 18]
print(adultos)
