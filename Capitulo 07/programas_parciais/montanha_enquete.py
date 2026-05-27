responses = {}
# Defina uma flag para indicar que a pesquisa está ativa.
polling_active = True

while polling_active:
    # Pergunte o nome da pessoa e a resposta.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Armazene a resposta no dicionário.
    responses[name] = response

    # Descubra se mais alguém vai participar da pesquisa.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# A pesquisa está completa. Mostre os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")