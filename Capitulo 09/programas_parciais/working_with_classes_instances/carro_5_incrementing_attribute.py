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
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode reverter um hodômetro!")

    def increment_odometer(self, miles):
        """Adicione o valor fornecido à leitura do hodômetro."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
