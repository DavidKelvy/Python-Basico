from pathlib import Path


path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Digite sua data de nascimento, no formato mmddyy: ")
if birthday in pi_string:
    print("Seu aniversário aparece no primeiro milhão de dígitos do pi!")
else:
    print("Seu aniversário não aparece no primeiro milhão de dígitos do pi.")