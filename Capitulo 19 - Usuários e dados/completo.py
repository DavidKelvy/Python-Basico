"""Capítulo 19: Usuários e permissões
Este arquivo mostra como armazenar dados de usuário e verificar acesso.
"""

usuarios = {
    'ana': {'senha': '1234', 'email': 'ana@example.com'},
    'bia': {'senha': 'abcd', 'email': 'bia@example.com'},
}
usuario = 'ana'
senha = '1234'

if usuario in usuarios and usuarios[usuario]['senha'] == senha:
    print('Login bem-sucedido')
else:
    print('Usuário ou senha inválidos')
