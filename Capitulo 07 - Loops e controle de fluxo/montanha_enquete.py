responses = {}
# Defina uma flag para indicar que a pesquisa está ativa.
polling_active = True

while polling_active:
    # Pergunte o nome da pessoa e a resposta.
    name = input("\nWhat is your name? ")
    response = input("Qual montanha você gostaria de escalar algum dia? ")

    # Armazene a resposta no dicionário.
    responses[name] = response

    # Descubra se mais alguém vai participar da pesquisa.
    repeat = input("Você gostaria de deixar outra pessoa responder? (sim/não) ")
    if repeat == 'no':
        polling_active = False

# A pesquisa está completa. Mostre os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")