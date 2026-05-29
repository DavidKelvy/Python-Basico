from name_function import get_formatted_name


print("Digite 'q' a qualquer momento para sair.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Por favor, me dê um sobrenome: ")
    if last == 'q':
        break
        
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")