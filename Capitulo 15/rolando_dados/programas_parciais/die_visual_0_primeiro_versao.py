from die import Die

# Crie um D6.
die = Die()

# Faça algumas jogadas e armazene os resultados em uma lista.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)