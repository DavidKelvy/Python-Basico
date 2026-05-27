print("Dê-me dois números e eu os dividirei.")
print("Digite 'q' para sair.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Segundo número: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)