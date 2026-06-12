# Capítulo 02 — Strings e variáveis (detalhado)

1) Strings
- Criação: `'texto'`, "texto", '''texto""'.
- Indexação e slicing:

```python
s = 'python'
print(s[0])   # 'p'
print(s[-1])  # 'n'
print(s[1:4]) # 'yth'
```

2) Métodos úteis
- `.strip()`, `.split()`, `.join()`, `.replace()`, `.lower()`, `.upper()`.

```python
nome = ' Ana ' 
print(nome.strip())
print('a,b,c'.split(','))
```

3) Formatação
- f-strings: `f"{nome} tem {idade} anos"`.

4) Escape sequences
- `\n`, `\t`, `\\`.

5) Variáveis e boas práticas
- Nomes claros, `snake_case`, evitar sobrescrever builtins.

6) Entrada do usuário

```python
nome = input('Nome: ')
print(f'Olá, {nome}')
```

Dica: use métodos de string para limpar entrada antes de processar.
