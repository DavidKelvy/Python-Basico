usuario = {'nome': 'Carla', 'idade': 29, 'cidade': 'Rio'}
usuario['profissao'] = 'Engenheira'
idade = usuario.get('idade')
chaves = list(usuario.keys())
valores = list(usuario.values())
items = list(usuario.items())
tupla = ('python', 'java', 'c++')
conjunto = {'maçã', 'banana', 'laranja'}
conjunto.add('uva')
conjunto.discard('banana')
intersecao = conjunto.intersection({'uva', 'pera'})
print(usuario)
print(idade)
print(chaves)
print(valores)
print(items)
print(tupla)
print(conjunto)
print(intersecao)
