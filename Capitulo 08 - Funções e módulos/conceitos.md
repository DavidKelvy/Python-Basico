# Capítulo 08 — Funções e módulos

Este capítulo mostra como organizar código com funções e arquivos.

## def
- `def nome(param):` define uma função.
- Blocos dentro da função são indentados.

## return
- `return` devolve um valor da função.
- Pode ser `None` se não houver retorno explícito.

## Parâmetros e argumentos
- Parâmetros são nomes na definição.
- Argumentos são valores passados na chamada.
- Parâmetros padrão fornecem valores quando nada é passado.

## *args e **kwargs
- `*args` agrupa argumentos posicionais extras em uma tupla.
- `**kwargs` agrupa argumentos nomeados extras em um dicionário.

## Docstrings
- Documentam o propósito de funções e módulos.
- Ficam logo após a definição, entre três aspas.

## Importar módulos
- `import modulo`
- `from modulo import func`
- `import modulo as alias`

## Pacotes
- Pastas com `__init__.py` são pacotes Python.
- Permitem organizar vários módulos.

## __name__ == '__main__'
- Verifica se o script está sendo executado diretamente.
- Evita rodar código no momento do import.
