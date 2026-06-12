conteudo = 'Linha 1
Linha 2
Linha 3
'
with open('exemplo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)

try:
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    linhas = []
else:
    for linha in linhas:
        print(linha.strip())
finally:
    print('Operação finalizada')
