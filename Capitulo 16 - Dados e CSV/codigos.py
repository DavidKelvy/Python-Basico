import csv

dados = [
    {'nome': 'Ana', 'idade': '23'},
    {'nome': 'Bruno', 'idade': '28'},
]
with open('dados.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'idade'])
    escritor.writeheader()
    escritor.writerows(dados)

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    nomes = [linha['nome'] for linha in leitor]
print(nomes)
