nome = 'Lucas'
saudacao = 'Olá'
mensagem = saudacao + ', ' + nome + '!'
comprimento = len(mensagem)
primeira_letra = mensagem[0]
ultimos_caracteres = mensagem[-3:]
texto_maiusculo = mensagem.upper()
texto_minusculo = mensagem.lower()
texto_limpo = '  Python  '.strip()
texto_substituido = mensagem.replace('Olá', 'Oi')
partes = mensagem.split(', ')
print(mensagem)
print(comprimento)
print(primeira_letra)
print(ultimos_caracteres)
print(texto_maiusculo)
print(texto_minusculo)
print(texto_limpo)
print(texto_substituido)
print(partes)
