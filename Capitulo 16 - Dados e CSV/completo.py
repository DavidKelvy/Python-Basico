"""Capítulo 16: Dados e CSV
Este arquivo mostra como ler e manipular dados de arquivos CSV.
"""

import csv

with open('dados_exemplo_cap16.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['dia', 'temperatura'])
    writer.writerow(['1', '22'])
    writer.writerow(['2', '24'])

with open('dados_exemplo_cap16.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print('linha:', linha)
