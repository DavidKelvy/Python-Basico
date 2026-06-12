"""Capítulo 16: CSV e formatos de arquivo
Este complemento mostra como ler e processar dados de arquivos CSV.
"""

import csv

with open('dados_exemplo.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['data', 'temperatura'])
    escritor.writerow(['2024-01-01', '22'])
    escritor.writerow(['2024-01-02', '24'])

with open('dados_exemplo.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print('Linha CSV:', linha)
