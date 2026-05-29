"""Capítulo 01: Ambientes virtuais e gerenciamento de pacotes

Este arquivo explica como criar um ambiente virtual e instalar pacotes com pip.
"""

print('Este arquivo mostra comandos e conceitos para ambientes virtuais.')

print('\n1. Criar ambiente virtual no Windows:')
print('python -m venv .venv')

print('\n2. Ativar o ambiente virtual no Windows PowerShell:')
print('.venv\\Scripts\\Activate.ps1')

print('\n3. Ativar o ambiente virtual no Windows CMD:')
print('.venv\\Scripts\\activate.bat')

print('\n4. Instalar um pacote com pip:')
print('pip install nome_do_pacote')

print('\n5. Verificar pacotes instalados:')
print('pip list')

print('\n6. Salvar dependências em requirements.txt:')
print('pip freeze > requirements.txt')

print('\n7. Recriar ambiente a partir de requirements.txt:')
print('pip install -r requirements.txt')

print('\nImportante: use ambientes virtuais para manter dependências isoladas.')
