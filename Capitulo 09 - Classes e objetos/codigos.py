class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'{self.nome} tem {self.idade} anos.'

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f'{self.nome} estuda {self.curso} e tem {self.idade} anos.'

pessoa = Pessoa('João', 28)
aluno = Aluno('Mariana', 21, 'Matemática')
print(pessoa.apresentar())
print(aluno.apresentar())
