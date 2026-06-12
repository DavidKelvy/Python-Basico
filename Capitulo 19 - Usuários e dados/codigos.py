usuarios = [
    {'nome': 'Alice', 'email': 'alice@example.com', 'idade': 24},
    {'nome': 'Bruno', 'email': 'bruno@example.com', 'idade': 30},
]
usuario_novo = {'nome': 'Carlos', 'email': 'carlos@example.com', 'idade': 27}
usuarios.append(usuario_novo)
emails = [usuario['email'] for usuario in usuarios]
adultos = [usuario for usuario in usuarios if usuario['idade'] >= 18]
print(usuarios)
print(emails)
print(adultos)
