"""Capítulo 07: Laços, while e controle de fluxo
Este complemento reúne exemplos de loops e controles interrompendo ou pulando iterações.
"""

# Loop while com condição de saída
contador = 0
while contador < 5:
    contador += 1
    print('Passo', contador)

# Usar break
for numero in range(1, 10):
    if numero == 5:
        print('Chegou em 5, saindo do loop')
        break
    print(numero)

# Usar continue
for numero in range(1, 6):
    if numero % 2 == 0:
        continue
    print('Ímpar:', numero)

# Loop e condicional juntos
palavras = ['cachorro', 'gato', 'elefante']
for palavra in palavras:
    if len(palavra) > 5:
        print(palavra, 'é longa')
    else:
        print(palavra, 'é curta')
