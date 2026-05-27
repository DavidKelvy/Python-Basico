class Car:
    """Uma simples tentativa de representar um carro."""

    def __init__(self, make, model, year):
        """Inicialize atributos para descrever um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorne um nome descritivo bem formatado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Imprima um extrato mostrando a quilometragem do carro."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Defina a leitura do hodômetro para o valor fornecido."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode reverter um hodômetro!")

    def increment_odometer(self, miles):
        """Adicione o valor fornecido à leitura do hodômetro."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Representam aspectos de um carro, específicos para veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Imprima uma declaração descrevendo o tamanho da bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()