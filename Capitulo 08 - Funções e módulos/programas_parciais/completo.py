"""Capítulo 08: Funções e importação
Este complemento cobre definições de funções, parâmetros e chamadas simples.
"""

# Definir função simples

def saudacao(nome):
    return f'Olá, {nome}!'

print(saudacao('Ana'))

# Parâmetros padrão

def fazer_saudacao(nome, saudacao='Olá'):
    return f'{saudacao}, {nome}!'

print(fazer_saudacao('Bia'))
print(fazer_saudacao('Carlos', saudacao='Oi'))

# Argumentos arbitrários

def listar_frutas(*frutas):
    for fruta in frutas:
        print('Fruta:', fruta)

listar_frutas('maçã', 'banana', 'laranja')

# Argumentos com palavras-chave

def exibir_usuario(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

exibir_usuario(nome='Luiza', idade=30)
