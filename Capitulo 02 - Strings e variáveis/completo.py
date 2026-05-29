"""Capítulo 02: Strings e texto
Este arquivo reúne exemplos básicos de manipulação de texto.
"""

nome = 'José'
print('O nome é', nome)
print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())
print('Tamanho:', len(nome))
print('Substituir:', nome.replace('é', 'e'))

mensagem = f'Olá, {nome}! Seja bem-vindo.'
print(mensagem)

texto = '   Python é ótimo   '
print('Texto original:', repr(texto))
print('Sem espaços:', texto.strip())
print('Começa com P?', texto.strip().startswith('Python'))
