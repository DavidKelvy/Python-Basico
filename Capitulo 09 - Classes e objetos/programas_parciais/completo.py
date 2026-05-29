"""Capítulo 09: Classes e objetos
Este complemento mostra as formas básicas de criar classes e usar herança.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Meu nome é {self.nome} e tenho {self.idade} anos.'

p = Pessoa('Luiz', 29)
print(p.apresentar())

# Herança

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f'Nome: {self.nome}, idade: {self.idade}, curso: {self.curso}'

aluno = Estudante('Marina', 22, 'Matemática')
print(aluno.apresentar())
