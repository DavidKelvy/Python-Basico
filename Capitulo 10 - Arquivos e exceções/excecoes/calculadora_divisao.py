print("Dê-me dois números e eu os dividirei.")
print("Digite 'q' para sair.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Segundo número: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Você não pode dividir por 0!")
    else:
        print(answer)