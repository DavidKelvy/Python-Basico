# Exemplo 1: For com enumerate
cores = ['vermelho', 'verde', 'azul']
for i, cor in enumerate(cores, 1):
    print(i, cor)

# Exemplo 2: Continue
for n in range(1, 6):
    if n == 3:
        continue
    print(n)

# Exemplo 3: Break
for n in range(1, 6):
    if n == 4:
        break
    print(n)

# Exemplo 4: While
n = 0
while n < 3:
    print('valor', n)
    n += 1

# Exemplo 5: Else no loop
for x in range(2):
    print('passo', x)
else:
    print('sem interrupção')
