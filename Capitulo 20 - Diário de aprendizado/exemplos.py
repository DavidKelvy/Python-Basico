# Exemplo 1: Criar anotação
from datetime import datetime
entrada = f'{datetime.now().date()} - Estudei variáveis'
print(entrada)

# Exemplo 2: Salvar em arquivo
with open('aprendizado.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(entrada + '
')

# Exemplo 3: Ler histórico
topico = 'Python'
with open('aprendizado.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        if topico in linha:
            print(linha.strip())
