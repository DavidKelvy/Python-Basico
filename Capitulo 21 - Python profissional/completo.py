"""Capítulo 21: Python profissional

Este arquivo demonstra uma visão geral dos temas avançados incluídos neste capítulo.
"""

from pathlib_os_datetime import criar_ambiente_de_dados
from pacote_python.operacoes import multiplicar
from pacote_python.utilidades import formatar_texto
from decoradores_e_metaprogramacao import calcular_tempo

print('Python profissional: tópicos avançados e boas práticas.')
print('Multiplicação de pacote:', multiplicar(6, 7))
print(formatar_texto(' curso profissional de python '))

with criar_ambiente_de_dados() as caminho:
    print('Ambiente de dados criado em:', caminho)

resultado = calcular_tempo(lambda: sum(range(1, 1000000)))
print(f'Tempo de execução aproximado: {resultado:.4f} segundos')
