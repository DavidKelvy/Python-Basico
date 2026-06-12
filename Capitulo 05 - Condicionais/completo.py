"""Capítulo 05: Condicionais
Este arquivo mostra if, elif, else e operadores lógicos.
"""

nota = 8
if nota >= 7:
    print('Aprovado')
elif nota >= 4:
    print('Recuperação')
else:
    print('Reprovado')

idade = 17
if idade >= 18:
    print('Adulto')
else:
    print('Menor de idade')

cores = ['vermelho', 'verde', 'azul']
if 'verde' in cores and 'amarelo' not in cores:
    print('Tem verde e não tem amarelo')
