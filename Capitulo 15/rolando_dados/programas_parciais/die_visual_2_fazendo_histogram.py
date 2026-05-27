import plotly.express as px

from die import Die


# Crie um D6.
die = Die()

# Faça algumas jogadas e armazene os resultados em uma lista.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analise os resultados.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize os resultados.
fig = px.bar(x=poss_results, y=frequencies)
fig.show()