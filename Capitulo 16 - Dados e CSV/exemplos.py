# Exemplo 1: Escrever CSV
import csv
registros = [
    {'nome': 'Carlos', 'idade': '32'},
    {'nome': 'Lívia', 'idade': '27'},
]
with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'idade'])
    escritor.writeheader()
    escritor.writerows(registros)

# Exemplo 2: Ler CSV
with open('usuarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['nome'], linha['idade'])

# Exemplo 3: Filtrar
usuarios = [
    {'nome': 'Ana', 'idade': 23},
    {'nome': 'Bruno', 'idade': 18},
]
adultos = [u for u in usuarios if u['idade'] >= 18]
print(adultos)
