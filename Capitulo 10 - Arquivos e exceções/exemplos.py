# Exemplo 1: Escrever arquivo
with open('saida.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Primeira linha
Segunda linha
')

# Exemplo 2: Ler arquivo
with open('saida.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Exemplo 3: Tratar arquivo inexistente
try:
    with open('inexistente.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print('Arquivo não encontrado')

# Exemplo 4: Finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Divisão por zero')
finally:
    print('Sempre executa')
