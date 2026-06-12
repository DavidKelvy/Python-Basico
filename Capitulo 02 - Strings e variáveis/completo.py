"""Capítulo 02: Strings e texto
Este arquivo reúne exemplos de manipulação de texto e variáveis.
"""

# Exemplo de variável string
nome = 'José'
print('O nome é', nome)

# Métodos de string básicos
print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())
print('Title:', nome.title())

# Comprimento e substituição
print('Tamanho:', len(nome))
print('Substituir:', nome.replace('é', 'e'))

# Formatação com f-strings
mensagem = f'Olá, {nome}! Seja bem-vindo.'
print(mensagem)

# Trabalhando com espaços em branco
texto = '   Python é ótimo   '
print('Texto original:', repr(texto))
print('Sem espaços:', texto.strip())
print('Começa com Python?', texto.strip().startswith('Python'))

# Verificação de conteúdo
print('Contém "Py"?', 'Py' in texto)
print('Contém "java"?', 'java' in texto)
