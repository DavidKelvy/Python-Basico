# Comece com alguns designs que precisam ser impressos.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simule a impressão de cada desenho, até que não reste nenhum.
# Mova cada design para completed_models após imprimir.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Modelo de impressão: {current_design}")
    completed_models.append(current_design)

# Exiba todos os modelos concluídos.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)