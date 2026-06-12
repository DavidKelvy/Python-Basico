# Capítulo 09 — Classes e objetos (detalhado)

1) Classe básica

```python
class Carro:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo

	def exibir(self):
		return f'{self.marca} {self.modelo}'
```

2) Herança

```python
class CarroEletrico(Carro):
	def __init__(self, marca, modelo, carga):
		super().__init__(marca, modelo)
		self.carga = carga
```

3) Encapsulamento por convenção (`_` e `__`)

Dica: mantenha responsabilidades da classe coesas (SRP).
