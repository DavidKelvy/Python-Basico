def get_formatted_name(first_name, last_name):
    """Retorne um nome completo, bem formatado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Este é um loop infinito!
while True:
    print("\nPlease tell me your name:")
    f_name = input("Primeiro nome: ")
    l_name = input("Sobrenome: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")