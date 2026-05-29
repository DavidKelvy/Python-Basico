def get_formatted_name(first_name, last_name):
    """Retorne um nome completo, bem formatado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Este é um loop infinito!
while True:
    print("\nPlease tell me your name:")
    print("(digite 'q' a qualquer momento para sair)")

    f_name = input("Primeiro nome: ")
    if f_name == 'q':
        break

    l_name = input("Sobrenome: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")