class Dog:
    """Uma simples tentativa de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicialize os atributos de nome e idade."""
        self.name = name
        self.age = age

    def sit(self):
        """Simule um cachorro sentado em resposta a um comando."""
        print(f"{self.name} agora está sentado.")

    def roll_over(self):
        """Simule a rolagem em resposta a um comando."""
        print(f"{self.name} rolou!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")