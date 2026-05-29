"""Um conjunto de classes que podem ser usadas para representar carros elétricos."""

from car import Car


class Battery:
    """Uma simples tentativa de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=40):
        """Inicialize os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Imprima uma declaração descrevendo o tamanho da bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Imprima uma declaração sobre o alcance que esta bateria oferece."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Modela aspectos de um carro, específicos para veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()