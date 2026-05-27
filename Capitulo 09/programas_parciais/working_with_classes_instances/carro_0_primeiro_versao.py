class Car:
    """Uma simples tentativa de representar um carro."""

    def __init__(self, make, model, year):
        """Inicialize atributos para descrever um carro."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Retorne um nome descritivo bem formatado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())