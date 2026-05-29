"""Capítulo 10: Arquivos e exceções
Este complemento reúne leituras de arquivo, escrita e tratamento de erros.
"""

# Escrever em um arquivo
with open('saida_exemplo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1
')
    arquivo.write('Linha 2
')

# Ler um arquivo
with open('saida_exemplo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print('Lido:', linha.strip())

# Ler e tratar erros
try:
    with open('nao_existe.txt', 'r', encoding='utf-8') as arquivo:
        arquivo.read()
except FileNotFoundError:
    print('Arquivo não encontrado')

# Exceção genérica
try:
    valor = int('abc')
except ValueError:
    print('Valor inválido')
