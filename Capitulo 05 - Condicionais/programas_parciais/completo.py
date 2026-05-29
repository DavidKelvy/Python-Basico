"""Capítulo 05: Condicionais e lógica
Este complemento agrega formas de usar if, elif, else e expressões lógicas.
"""

# Estrutura if / elif / else
idade = 17
if idade < 13:
    print('Criança')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')

# Operadores lógicos
nota = 6.5
if nota >= 7 and nota <= 10:
    print('Aprovado')
elif nota >= 4 or nota == 3.5:
    print('Recuperação')
else:
    print('Reprovado')

# Testar presença em lista
ingredientes = ['queijo', 'tomate', 'manjericão']
if 'manjericão' in ingredientes:
    print('Tem manjericão')
else:
    print('Sem manjericão')

# Condicional simples
tem_ingressos = True
if tem_ingressos:
    print('Vamos ao parque')
else:
    print('Fica para outra hora')
