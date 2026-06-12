"""Capítulo 01: Strings e variáveis
Este arquivo mostra como criar variáveis e usar texto em Python.
"""

# Criar variáveis e nomes
nome = 'Ana'
idade = 18
altura = 1.65

# Imprimir valores
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)

# Texto simples
texto_simples = 'Olá, mundo!'
print(texto_simples)

# Concatenação de strings
saudacao = 'Olá, ' + nome + '!'
print(saudacao)

# f-strings para texto formatado
mensagem = f'{nome} tem {idade} anos e {altura}m de altura.'
print(mensagem)

# Converter tipos para texto
print('Idade como texto: ' + str(idade))

# Tipos de dados básicos
print(type(nome))
print(type(idade))
print(type(altura))
print(type(True))
