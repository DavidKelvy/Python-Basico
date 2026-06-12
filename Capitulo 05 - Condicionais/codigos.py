idade = 25
if idade < 12:
    fase = 'criança'
elif idade < 18:
    fase = 'adolescente'
elif idade < 60:
    fase = 'adulto'
else:
    fase = 'idoso'
nota = 8.2
aprovado = nota >= 7
mensagem = 'aprovado' if aprovado else 'reprovado'
acesso = idade >= 18 and aprovado
print(fase)
print(mensagem)
print('Acesso liberado:', acesso)
