# Capítulo 09 — Classes e objetos

Este capítulo introduz orientação a objetos.

## Classe
- Uma classe é um molde para criar objetos.
- Defina com `class Nome:`.

## Instância
- Um objeto criado a partir de uma classe.
- Use `obj = Classe()`.

## __init__
- Método construtor chamado ao criar a instância.
- Recebe `self` e outros parâmetros.

## Atributos
- Armazenam dados no objeto.
- Exemplo: `self.nome = nome`.

## Métodos
- Funções definidas dentro da classe.
- Usam `self` para acessar atributos e outros métodos.

## Herança
- Uma classe filha herda comportamento da classe pai.
- Use `class Filha(Pai):`.

## Encapsulamento
- `_atributo` indica uso interno.
- `__atributo` cria nome mangled para dificultar acesso externo.

## Composição
- Uma classe pode conter objetos de outra classe.
