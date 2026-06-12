"""Capítulo 08: Funções
Este arquivo mostra definições, parâmetros e chamadas de função.
"""

def saudacao(nome):
    return f'Olá, {nome}!'

print(saudacao('Ana'))


def somar(a, b=0):
    return a + b

print('5 + 3 =', somar(5, 3))
print('5 + 0 =', somar(5))


def listar_itens(*itens):
    for item in itens:
        print('Item:', item)

listar_itens('maçã', 'banana')


def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

mostrar_info(nome='João', idade=30)
