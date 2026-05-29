"""Capítulo 01: Conceitos básicos de Python
Este arquivo reúne os exemplos mais básicos para quem começa do zero.
"""

# Imprimir texto na tela
print('Olá, mundo!')
print("Python é divertido!")

# Comentários explicam o código e não são executados
# isto é um comentário de linha
"""Isto é uma string de várias linhas.
Elas podem ocupar mais de uma linha no código.
"""

# Variáveis armazenam valores
mensagem = 'Bem-vindo ao Python!'
print(mensagem)

# Números inteiros e ponto flutuante
idade = 20
peso = 68.5
print('Idade:', idade)
print('Peso:', peso)

# Operações aritméticas básicas
soma = 5 + 3
subtracao = 10 - 4
multiplicacao = 6 * 7
divisao = 20 / 5
potenciacao = 2 ** 3
resto = 10 % 3
divisao_inteira = 11 // 3
print('Soma:', soma)
print('Subtração:', subtracao)
print('Multiplicação:', multiplicacao)
print('Divisão:', divisao)
print('Potenciação:', potenciacao)
print('Resto:', resto)
print('Divisão inteira:', divisao_inteira)

# Ordem de precedência
resultado = 2 + 3 * 4
print('2 + 3 * 4 =', resultado)
resultado_parenteses = (2 + 3) * 4
print('(2 + 3) * 4 =', resultado_parenteses)

# Strings e concatenação
nome = 'Maria'
idade_texto = '18'
print('Olá, ' + nome + '!')
print(f'{nome} tem {idade_texto} anos.')

# Conversão de tipos
ano_nascimento = 2024 - idade
print('Ano de nascimento:', ano_nascimento)
print('Idade como texto: ' + str(idade))

# Tipos de dados básicos
print(type(idade))
print(type(peso))
print(type(nome))
print(type(True))

# Comparações e valores booleanos
print('5 é maior que 3?', 5 > 3)
print('10 é igual a 10?', 10 == 10)
print('7 é diferente de 8?', 7 != 8)

# Operadores lógicos
print('Verdadeiro e Falso:', True and False)
print('Verdadeiro ou Falso:', True or False)
print('Não Verdadeiro:', not True)

# Exemplo simples de condição
numero = 8
if numero % 2 == 0:
    print(numero, 'é par')
else:
    print(numero, 'é ímpar')

# Função simples

def dobrar(valor):
    return valor * 2

print('Dobro de 5:', dobrar(5))

# Estrutura de repetição simples
for i in range(1, 6):
    print('Contagem:', i)

# Exemplo de lista básica
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print('Fruta:', fruta)
