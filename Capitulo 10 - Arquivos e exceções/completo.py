"""Capítulo 10: Arquivos e exceções
Este arquivo mostra leitura, escrita e tratamento de erros.
"""

nome_arquivo = 'exemplo_cap10.txt'
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 2')

with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print('Lido:', linha.strip())

try:
    with open('arquivo_inexistente.txt', 'r', encoding='utf-8') as arquivo:
        arquivo.read()
except FileNotFoundError:
    print('Arquivo não encontrado')
