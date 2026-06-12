# Capítulo 02 — Strings e variáveis (completo)

Este capítulo mostra como trabalhar com texto em Python, como armazenar valores em variáveis, como formatar e transformar strings e como documentar o código.

## 1) Comentários e docstrings
- Comentários usam `#` e são ignorados na execução.
- Docstrings são strings triplas `"""..."""` usadas para descrever o propósito de um módulo, função ou classe.

Exemplo:
```python
# Diga olá a todos.
print('Olá pessoal do Python!')
```

## 2) Variáveis
- Variáveis recebem valores com `=`.
- Boa prática: use nomes descritivos em `snake_case`.
- Variáveis são mutáveis no sentido de que podem ser reassinadas.

Exemplo:
```python
message = 'Hello Python world!'
print(message)
message = 'Hello Python Crash Course world!'
print(message)
```

## 3) Strings
- Textos são valores do tipo `str`.
- Podem ser delimitados por aspas simples `'texto'` ou aspas duplas `"texto"`.
- String com apóstrofo pode usar aspas duplas para evitar escape.

Exemplo:
```python
message = "One of Python's strengths is its diverse community."
print(message)
```

## 4) Métodos de string
- `.title()`: capitaliza cada palavra.
- `.upper()`: converte para maiúsculas.
- `.lower()`: converte para minúsculas.
- `.replace(old, new)`: substitui texto.
- `.strip()`: remove espaços em branco do início e fim.
- `.startswith(prefix)`: verifica prefixo.

Exemplo:
```python
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())
```

## 5) Funções de string e tamanho
- `len(string)` retorna o comprimento.
- `repr(string)` mostra a representação literal da string, útil para depuração.

Exemplo:
```python
text = '   Python é ótimo   '
print(len(text))
print(repr(text))
```

## 6) Formatação de strings
- F-strings (`f"..."`) permitem inserir valores diretamente.
- Use expressões dentro das chaves.

Exemplo:
```python
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(f'Hello, {full_name.title()}!')
```

## 7) Print com múltiplos argumentos
- `print()` aceita vários valores separados por vírgula.
- O Python inclui um espaço automaticamente entre argumentos.

Exemplo:
```python
nome = 'José'
print('O nome é', nome)
```

## 8) Controle de formato de strings
- Use `strip()` para limpar espaços extras.
- Use `startswith()` para verificar prefixos.
- Combine métodos para transformar texto antes de mostrar ou comparar.

Exemplo:
```python
texto = '   Python é ótimo   '
print(texto.strip())
print(texto.strip().startswith('Python'))
```

## 9) Boas práticas deste capítulo
- Mantenha variáveis e strings legíveis.
- Use métodos de string em vez de manipulação manual quando possível.
- Prefira f-strings para interpolação de valores.
- Documente o propósito do arquivo com docstrings no início.

Este conteúdo reúne todos os conceitos usados nos exemplos do capítulo 2 e fornece explicações e exemplos para cada um deles.
