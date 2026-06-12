# Exemplo 1: Classe Carro
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def descricao(self):
        return f'{self.marca} ({self.ano})'
meu_carro = Carro('Fiat', 2020)
print(meu_carro.descricao())

# Exemplo 2: Herança
class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

class Moto(Veiculo):
    def __init__(self, tipo, cilindrada):
        super().__init__(tipo)
        self.cilindrada = cilindrada

m = Moto('motocicleta', 250)
print(m.tipo, m.cilindrada)

# Exemplo 3: Conta bancária
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

c = Conta(100)
c.depositar(50)
c.sacar(30)
print(c.saldo)
