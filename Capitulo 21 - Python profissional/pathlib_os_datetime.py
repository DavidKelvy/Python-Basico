"""Uso profissional de pathlib, os e datetime.
"""

from pathlib import Path
from datetime import datetime
import os

caminho_projeto = Path.cwd() / 'dados_profissionais'
print('Caminho do projeto:', caminho_projeto)

if not caminho_projeto.exists():
    caminho_projeto.mkdir(parents=True)
    print('Diretório criado:', caminho_projeto)
else:
    print('Diretório já existe')

arquivo_exemplo = caminho_projeto / 'exemplo.txt'
with arquivo_exemplo.open('w', encoding='utf-8') as arquivo:
    arquivo.write('Dados de exemplo para o curso profissional\n')

print('Arquivo salvo em:', arquivo_exemplo)
print('Arquivo existe?', arquivo_exemplo.exists())
print('É arquivo?', arquivo_exemplo.is_file())

print('Usuário atual:', os.getenv('USERNAME') or os.getenv('USER'))
print('Hora atual:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


from contextlib import contextmanager

@contextmanager
def criar_ambiente_de_dados():
    pasta = Path.cwd() / 'dados_temp'
    pasta.mkdir(exist_ok=True)
    try:
        yield pasta
    finally:
        if pasta.exists():
            for filho in pasta.iterdir():
                filho.unlink()
            pasta.rmdir()


if __name__ == '__main__':
    with criar_ambiente_de_dados() as caminho:
        arquivo = caminho / 'teste.txt'
        arquivo.write_text('Ambiente temporário de dados.', encoding='utf-8')
        print('Criado arquivo em:', arquivo)
