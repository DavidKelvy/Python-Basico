from datetime import datetime

def criar_entrada(texto):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'{agora} - {texto}'

entrada = criar_entrada('Hoje estudei Python e organizei o projeto.')
with open('diario.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(entrada + '
')

with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
