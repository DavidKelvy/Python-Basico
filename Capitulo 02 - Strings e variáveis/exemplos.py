# Exemplo 1: Criar nomes completos
primeiro_nome = 'Beatriz'
ultimo_nome = 'Souza'
nome_completo = primeiro_nome + ' ' + ultimo_nome
print(nome_completo)

# Exemplo 2: F-strings
genero = 'feminino'
idade = 28
resumo = f'{nome_completo} tem {idade} anos e gênero {genero}.'
print(resumo)

# Exemplo 3: Fatiamento
texto = 'programacao'
print(texto[0:4])
print(texto[-6:])

# Exemplo 4: Métodos
frase = '  aula de python  '
print(frase.strip())
print(frase.title())
print(frase.replace('python', 'programação'))

# Exemplo 5: Conversão
numero_texto = '100'
numero_inteiro = int(numero_texto)
print(numero_inteiro * 2)
