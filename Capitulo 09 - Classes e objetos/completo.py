"""Capítulo 09: Classes e objetos
Este arquivo mostra o básico de classes em Python.
"""

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f'{self.nome} está fazendo barulho.'


class Cachorro(Animal):
    def falar(self):
        return f'{self.nome} está latindo.'

pet = Cachorro('Bolt', 5)
print(pet.falar())
print(pet.nome, 'tem', pet.idade, 'anos')
