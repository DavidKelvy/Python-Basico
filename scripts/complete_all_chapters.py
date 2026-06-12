from pathlib import Path
import shutil

root = Path('c:/Users/davidsantos/Documents/GitHub/Python-Basico')

chapters = {
    '01': {
        'title': 'Fundamentos básicos',
        'explicacao': """# Fundamentos básicos

Este capítulo apresenta os conceitos essenciais para começar a programar em Python.

## O que é Python

Python é uma linguagem de alto nível, interpretada e de fácil leitura. Ela foi criada para ser clara e produtiva.

## Ambiente e execução

Um programa Python é um arquivo de texto com extensão `.py`. O interpretador lê e executa cada linha em sequência.

## Variáveis e tipos de dados

Uma variável associa um nome a um valor. Python reconhece tipos como inteiro, ponto flutuante, string e booleano.

## Operadores básicos

- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`

## Entrada e saída

`print()` mostra resultados no terminal. `input()` lê dados do usuário como texto.

## Estrutura

A indentação define blocos de código em Python, por isso é importante usar espaços ou tabulação de forma consistente.

## Exemplos de uso

Programas simples mostram texto, fazem cálculos e exibem resultados. Esse é o primeiro passo para aprender lógica.
""",
        'codigos': """print('Olá Mundo')
idade = 30
altura = 1.75
nome = 'Ana'
area = altura * 2
idade_em_anos = idade
mensagem = f'{nome} tem {idade_em_anos} anos e mede {altura} m.'
resultado = idade + area
condicao = idade >= 18
print(mensagem)
print('Área:', area)
print('Resultado:', resultado)
print('Maior de idade?', condicao)
""",
        'exemplos': """# Exemplo 1: Olá Mundo
print('Olá, Python!')

# Exemplo 2: Variáveis e tipos
nome = 'Lucas'
idade = 22
altura = 1.82
print(nome, idade, altura)

# Exemplo 3: Operações matemáticas
soma = idade + 5
subtracao = idade - 10
multiplicacao = altura * 2
divisao = idade / 2
print(soma, subtracao, multiplicacao, divisao)

# Exemplo 4: Conversão de tipos
numero = '10'
numero_int = int(numero)
print(numero_int + 5)

# Exemplo 5: Entrada de usuário
# usuario = input('Digite seu nome: ')
# print('Olá,', usuario)
""",
    },
    '02': {
        'title': 'Strings e variáveis',
        'explicacao': """# Strings e variáveis

Neste capítulo você aprende a trabalhar com texto e a armazenar dados com clareza.

## Strings

Strings são sequências de caracteres. Podem ser criadas com aspas simples, duplas ou triplas.

## Concatenar e formatar

É possível juntar strings com `+` ou criar textos interpolados com f-strings.

## Métodos de string

- `strip()` remove espaços em branco.
- `upper()` converte para maiúsculas.
- `lower()` converte para minúsculas.
- `replace()` troca partes do texto.
- `split()` divide a string em pedaços.

## Variáveis

Uma variável guarda o valor atual. O mesmo nome pode receber diferentes tipos, mas é melhor manter consistência.

## Boas práticas

Use nomes significativos e evite abreviações confusas. Strings longas devem ficar legíveis.
""",
        'codigos': """nome = 'Lucas'
saudacao = 'Olá'
mensagem = saudacao + ', ' + nome + '!'
comprimento = len(mensagem)
primeira_letra = mensagem[0]
ultimos_caracteres = mensagem[-3:]
texto_maiusculo = mensagem.upper()
texto_minusculo = mensagem.lower()
texto_limpo = '  Python  '.strip()
texto_substituido = mensagem.replace('Olá', 'Oi')
partes = mensagem.split(', ')
print(mensagem)
print(comprimento)
print(primeira_letra)
print(ultimos_caracteres)
print(texto_maiusculo)
print(texto_minusculo)
print(texto_limpo)
print(texto_substituido)
print(partes)
""",
        'exemplos': """# Exemplo 1: Criar nomes completos
primeiro_nome = 'Beatriz'
ultimo_nome = 'Souza'
nome_completo = primeiro_nome + ' ' + ultimo_nome
print(nome_completo)

# Exemplo 2: F-strings
genero = 'feminino'
idade = 28
resumo = f'{nome_completo} tem {idade} anos e gênero {genero}.'
print(resumo)

# Exemplo 3: Fatiamento
texto = 'programacao'
print(texto[0:4])
print(texto[-6:])

# Exemplo 4: Métodos
frase = '  aula de python  '
print(frase.strip())
print(frase.title())
print(frase.replace('python', 'programação'))

# Exemplo 5: Conversão
numero_texto = '100'
numero_inteiro = int(numero_texto)
print(numero_inteiro * 2)
""",
    },
    '03': {
        'title': 'Listas',
        'explicacao': """# Listas

Listas armazenam várias informações ordenadas em uma única variável.

## Criação de listas

Use colchetes `[]` para definir uma lista. Elementos são separados por vírgula.

## Acessar elementos

Cada item tem um índice: o primeiro é 0, o último é -1.

## Métodos úteis

- `append()` adiciona ao final.
- `insert()` insere em posição específica.
- `remove()` exclui um item.
- `pop()` remove o item e retorna ele.
- `sort()` ordena.

## Listas heterogêneas

Uma lista pode conter inteiros, strings e outros objetos juntos.

## Compreensões

Listas podem ser criadas de forma concisa com compreensões.
""",
        'codigos': """cores = ['vermelho', 'verde', 'azul']
cores.append('amarelo')
cores.insert(1, 'laranja')
cores.remove('verde')
ultimo = cores.pop()
contador = len(cores)
ordenado = sorted(cores)
cores.sort()
cores.reverse()
quadrados = [n * n for n in range(1, 6)]
pares = [n for n in range(1, 11) if n % 2 == 0]
print(cores)
print(ultimo)
print(contador)
print(ordenado)
print(quadrados)
print(pares)
""",
        'exemplos': """# Exemplo 1: Acessar itens
frutas = ['maçã', 'banana', 'uva']
print(frutas[0])
print(frutas[-1])

# Exemplo 2: Adicionar e remover
frutas.append('laranja')
frutas.remove('banana')
print(frutas)

# Exemplo 3: Iterar com for
for fruta in frutas:
    print('Fruta:', fruta)

# Exemplo 4: Compreensão
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print(quadrados)

# Exemplo 5: Ordenação
valores = [9, 3, 6, 1]
valores.sort()
print(valores)
""",
    },
    '04': {
        'title': 'Laços e operações numéricas',
        'explicacao': """# Laços e operações numéricas

Aqui combinamos repetição com cálculo para resolver tarefas mais complexas.

## For e while

`for` percorre sequências. `while` repete enquanto uma condição for verdadeira.

## Operadores numéricos

- `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Ordem de precedência funciona como nas matemáticas.

## Controle de fluxo

`break` interrompe o loop. `continue` pula para a próxima rodada.

## Range

`range()` gera sequências de números usadas em loops.

## Aplicações

Soma de valores, contador de pares, geração de tabelas e cálculo de médias.
""",
        'codigos': """numeros = [1, 2, 3, 4, 5]
total = 0
for n in numeros:
    total += n
media = total / len(numeros)
pares = [n for n in range(1, 11) if n % 2 == 0]
produto = 1
for n in range(1, 6):
    produto *= n
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    if contador == 5:
        break
print('Total:', total)
print('Média:', media)
print('Pares:', pares)
print('Fatorial:', produto)
""",
        'exemplos': """# Exemplo 1: Soma com loop
valores = [10, 20, 30]
acumulado = 0
for valor in valores:
    acumulado += valor
print(acumulado)

# Exemplo 2: Pares com range
for n in range(1, 11):
    if n % 2 == 0:
        print(n, 'é par')

# Exemplo 3: Loop while
contador = 1
while contador <= 4:
    print(contador)
    contador += 1

# Exemplo 4: Break e continue
for n in range(1, 6):
    if n == 2:
        continue
    if n == 5:
        break
    print(n)

# Exemplo 5: Compreensão numérica
cubos = [x ** 3 for x in range(1, 6)]
print(cubos)
""",
    },
    '05': {
        'title': 'Condicionais',
        'explicacao': """# Condicionais

Condicionais permitem escolher entre diferentes rotas de execução.

## If, elif e else

`if` executa um bloco quando a condição é verdadeira. `elif` adiciona novas verificações. `else` cobre o resto.

## Operadores de comparação

- Igualdade: `==`
- Diferença: `!=`
- Maior/menor: `>`, `<`, `>=`, `<=`

## Operadores lógicos

- `and` exige todas verdadeiras.
- `or` exige pelo menos uma verdadeira.
- `not` inverte o valor.

## Validação de dados

Condicionais também verificam entradas do usuário e evitam erros.

## Estruturas encadeadas

Aninhar condicionais deve ser feito com cuidado para não perder legibilidade.
""",
        'codigos': """idade = 25
if idade < 12:
    fase = 'criança'
elif idade < 18:
    fase = 'adolescente'
elif idade < 60:
    fase = 'adulto'
else:
    fase = 'idoso'
nota = 8.2
aprovado = nota >= 7
mensagem = 'aprovado' if aprovado else 'reprovado'
acesso = idade >= 18 and aprovado
print(fase)
print(mensagem)
print('Acesso liberado:', acesso)
""",
        'exemplos': """# Exemplo 1: Ímpar ou par
numero = 7
if numero % 2 == 0:
    print('par')
else:
    print('ímpar')

# Exemplo 2: Faixas de nota
pontuacao = 72
if pontuacao >= 90:
    print('excelente')
elif pontuacao >= 70:
    print('bom')
else:
    print('precisa melhorar')

# Exemplo 3: Operadores lógicos
a = True
b = False
if a and not b:
    print('Condição satisfeita')

# Exemplo 4: Expressão condicional
texto = 'aprovado' if pontuacao >= 70 else 'reprovado'
print(texto)

# Exemplo 5: Comparação composta
x = 15
if 10 < x <= 20:
    print('x está entre 11 e 20')
""",
    },
    '06': {
        'title': 'Dicionários e coleções',
        'explicacao': """# Dicionários e coleções

Aqui estudamos estruturas para armazenar dados com chaves e valores.

## Dicionários

Dicionários representam registros e mapas de dados.

## Tuplas

Tuplas são como listas, mas imutáveis.

## Conjuntos

Sets armazenam valores únicos e permitem operações matemáticas como união e interseção.

## Métodos importantes

- `dict.keys()`, `dict.values()`, `dict.items()`
- `set.add()`, `set.discard()`, `set.union()`
- `tuple()` e `list()` para conversões.

## Uso prático

Dicionários são ideais para armazenar informações de usuários, produtos ou configurações.
""",
        'codigos': """usuario = {'nome': 'Carla', 'idade': 29, 'cidade': 'Rio'}
usuario['profissao'] = 'Engenheira'
idade = usuario.get('idade')
chaves = list(usuario.keys())
valores = list(usuario.values())
items = list(usuario.items())
tupla = ('python', 'java', 'c++')
conjunto = {'maçã', 'banana', 'laranja'}
conjunto.add('uva')
conjunto.discard('banana')
intersecao = conjunto.intersection({'uva', 'pera'})
print(usuario)
print(idade)
print(chaves)
print(valores)
print(items)
print(tupla)
print(conjunto)
print(intersecao)
""",
        'exemplos': """# Exemplo 1: Dicionário simples
pessoa = {'nome': 'Pedro', 'idade': 34}
print(pessoa['nome'])

# Exemplo 2: Atualizar e remover
pessoa['idade'] = 35
pessoa.pop('idade')
print(pessoa)

# Exemplo 3: Tupla
coordenadas = (10.5, 20.3)
print(coordenadas)

# Exemplo 4: Conjunto
frutas = {'maçã', 'banana', 'maçã'}
print(frutas)

# Exemplo 5: Interseção
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.intersection(b))
""",
    },
    '07': {
        'title': 'Loops e controle de fluxo',
        'explicacao': """# Loops e controle de fluxo

Este capítulo explica como repetir tarefas usando laços e como controlar o caminho do programa.

## For

Use `for` para percorrer sequências como listas ou strings.

## While

Use `while` quando não souber o número exato de repetições.

## Break e continue

`break` encerra o loop. `continue` pula para a próxima iteração.

## Else em loops

O bloco `else` executa quando o loop termina sem interrupção.

## Iteradores

Strings, listas e range são iteráveis e funcionam com `for`.
""",
        'codigos': """nomes = ['Ana', 'Bruno', 'Carla']
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)

pares = []
for n in range(1, 11):
    if n % 2 != 0:
        continue
    pares.append(n)
else:
    print('Loop for finalizado')

contador = 0
while contador < 5:
    if contador == 3:
        break
    contador += 1
print(pares)
""",
        'exemplos': """# Exemplo 1: For com enumerate
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
""",
    },
    '08': {
        'title': 'Funções e módulos',
        'explicacao': """# Funções e módulos

Funções permitem reutilizar lógica e módulos ajudam a organizar código.

## Definir funções

Use `def nome(parametros):` para declarar funções.

## Parâmetros e retorno

Uma função pode receber valores e devolver resultados com `return`.

## Escopo

Variáveis dentro da função são locais. Variáveis fora são globais.

## Módulos

Importe código de outros arquivos com `import` ou `from ... import ...`.

## Prática

Separe lógica em funções para tornar o programa mais legível e testável.
""",
        'codigos': """def saudacao(nome, saudacao='Olá'):
    return f'{saudacao}, {nome}!'

def soma(a, b=0):
    return a + b

resultado1 = saudacao('Lucas')
resultado2 = saudacao('Mariana', 'Bom dia')
valor1 = soma(3, 7)
valor2 = soma(5)

import math
import random

raiz = math.sqrt(16)
aleatorio = random.randint(1, 10)
print(resultado1)
print(resultado2)
print(valor1)
print(valor2)
print(raiz)
print(aleatorio)
""",
        'exemplos': """# Exemplo 1: Função simples
def dobrar(valor):
    return valor * 2
print(dobrar(4))

# Exemplo 2: Parâmetro padrão
def apresentar(nome='visitante'):
    return f'Olá, {nome}!'
print(apresentar())
print(apresentar('Rita'))

# Exemplo 3: Importar módulo
import math
print(math.pi)
print(math.factorial(5))

# Exemplo 4: Função por nome
def soma(a, b):
    return a + b
print(soma(b=2, a=3))

# Exemplo 5: Retornar lista
def pares_ate(n):
    return [x for x in range(1, n + 1) if x % 2 == 0]
print(pares_ate(10))
""",
    },
    '09': {
        'title': 'Classes e objetos',
        'explicacao': """# Classes e objetos

A orientação a objetos modela dados e comportamentos através de classes.

## Classe e instância

Classe define um tipo de objeto. Instância é um objeto criado a partir dela.

## Atributos e métodos

Atributos são dados. Métodos são funções ligadas ao objeto.

## Construtor

`__init__` inicializa o estado do objeto.

## Herança

Uma classe filha herda atributos e métodos da classe pai.

## Polimorfismo

Diferentes classes podem implementar métodos com o mesmo nome.
""",
        'codigos': """class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'{self.nome} tem {self.idade} anos.'

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f'{self.nome} estuda {self.curso} e tem {self.idade} anos.'

pessoa = Pessoa('João', 28)
aluno = Aluno('Mariana', 21, 'Matemática')
print(pessoa.apresentar())
print(aluno.apresentar())
""",
        'exemplos': """# Exemplo 1: Classe Carro
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def descricao(self):
        return f'{self.marca} ({self.ano})'
meu_carro = Carro('Fiat', 2020)
print(meu_carro.descricao())

# Exemplo 2: Herança
class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

class Moto(Veiculo):
    def __init__(self, tipo, cilindrada):
        super().__init__(tipo)
        self.cilindrada = cilindrada

m = Moto('motocicleta', 250)
print(m.tipo, m.cilindrada)

# Exemplo 3: Conta bancária
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

c = Conta(100)
c.depositar(50)
c.sacar(30)
print(c.saldo)
""",
    },
    '10': {
        'title': 'Arquivos e exceções',
        'explicacao': """# Arquivos e exceções

Este capítulo ensina a gravar dados em arquivos e a tratar erros.

## Abrir arquivos

Use `open()` com modos como `'r'`, `'w'`, `'a'` e `'x'`.

## Leitura e escrita

- `read()`: lê todo o conteúdo.
- `readline()`: lê uma linha.
- `readlines()`: lê todas as linhas.
- `write()`: grava texto.

## With

`with` garante que o arquivo seja fechado automaticamente.

## Exceções

Use `try`, `except`, `else` e `finally` para tratar problemas.

## Erros comuns

- `FileNotFoundError`
- `ZeroDivisionError`
- `ValueError`
""",
        'codigos': """conteudo = 'Linha 1\nLinha 2\nLinha 3\n'
with open('exemplo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)

try:
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    linhas = []
else:
    for linha in linhas:
        print(linha.strip())
finally:
    print('Operação finalizada')
""",
        'exemplos': """# Exemplo 1: Escrever arquivo
with open('saida.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Primeira linha\nSegunda linha\n')

# Exemplo 2: Ler arquivo
with open('saida.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Exemplo 3: Tratar arquivo inexistente
try:
    with open('inexistente.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print('Arquivo não encontrado')

# Exemplo 4: Finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Divisão por zero')
finally:
    print('Sempre executa')
""",
    },
    '11': {
        'title': 'Funções e testes',
        'explicacao': """# Funções e testes

Neste capítulo você aprende a criar funções reutilizáveis e testar se elas funcionam.

## Funções

Funções organizam código em blocos que recebem entradas e retornam saídas.

## Parâmetros posicionais e nomeados

Funções podem aceitar parâmetros na ordem ou por nome.

## Valores padrão

Defina valores padrão para parâmetros opcionais.

## Testes com assert

`assert` verifica se uma condição é verdadeira e gera erro em caso contrário.

## Mock de comportamento

Testes simples ajudam a encontrar erros rapidamente.
""",
        'codigos': """def soma(a, b):
    return a + b

def maior(a, b):
    return a if a >= b else b

def eh_par(n):
    return n % 2 == 0

assert soma(2, 3) == 5
assert maior(7, 4) == 7
assert maior(3, 5) == 5
assert eh_par(4) is True
assert eh_par(5) is False
print('Testes básicos executados com sucesso')
""",
        'exemplos': """# Exemplo 1: Criar função
def dobro(valor):
    return valor * 2
print(dobro(5))

# Exemplo 2: Parâmetros padrão
def saudacao(nome='visitante'):
    return f'Olá, {nome}!'
print(saudacao())
print(saudacao('Luna'))

# Exemplo 3: Testes
assert dobro(2) == 4
assert saudacao('Ana') == 'Olá, Ana!'
print('Assert passou')

# Exemplo 4: Filtrar lista
def pares(lista):
    return [x for x in lista if x % 2 == 0]
print(pares([1, 2, 3, 4]))
""",
    },
    '12': {
        'title': 'Projeto de jogo',
        'explicacao': """# Projeto de jogo

Este capítulo mostra como montar um jogo simples em etapas organizadas.

## Estrutura do jogo

- Inicializar estado
- Receber ações do jogador
- Atualizar variáveis
- Verificar condições de fim

## Separação em funções

Divida a lógica em funções para tornar o jogo mais claro.

## Pontuação e vidas

Controle de pontos e vidas são elementos centrais em jogos simples.

## Ciclo principal

O loop principal repete até o jogo terminar.

## Testar o fluxo

Teste cada parte separadamente antes de unir o jogo completo.
""",
        'codigos': """def iniciar_jogo():
    vidas = 3
    pontos = 0
    nivel = 1
    return vidas, pontos, nivel

def atualizar_jogo(pontos, nivel, inimigos):
    pontos += inimigos * 10
    if pontos >= nivel * 50:
        nivel += 1
    return pontos, nivel

def jogo_ativo(vidas):
    return vidas > 0

vidas, pontos, nivel = iniciar_jogo()
vidas -= 1
pontos, nivel = atualizar_jogo(pontos, nivel, 4)
print('Vidas:', vidas)
print('Pontos:', pontos)
print('Nível:', nivel)
print('Jogo ativo:', jogo_ativo(vidas))
""",
        'exemplos': """# Exemplo 1: Estado do jogo
game = {'vidas': 3, 'pontos': 0, 'nivel': 1}
print(game)

# Exemplo 2: Atualizar pontuação
game['pontos'] += 25
print(game['pontos'])

# Exemplo 3: Subir de nível
if game['pontos'] >= 50:
    game['nivel'] += 1
print(game['nivel'])

# Exemplo 4: Verificar fim de jogo
if game['vidas'] == 0:
    print('Game Over')
else:
    print('Continue jogando')
""",
    },
    '13': {
        'title': 'Jogo com alienígenas',
        'explicacao': """# Jogo com alienígenas

Este capítulo desenvolve entidades, ataques e lógica de jogo com temas de alienígenas.

## Inimigos

Cada alienígena tem posição, vida e comportamento simples.

## Jogador

O jogador interage com o ambiente e afeta o estado dos inimigos.

## Ataque e pontuação

Ao derrotar um inimigo, o jogador ganha pontos.

## Atualizar estado

A cada rodada, o jogo atualiza vidas, posições e pontuação.

## Regras simples

Comece com regras básicas e adicione complexidade gradualmente.
""",
        'codigos': """class Alien:
    def __init__(self, x, y, vida):
        self.x = x
        self.y = y
        self.vida = vida

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def sofrer_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

class Jogador:
    def __init__(self):
        self.pontuacao = 0

    def atacar(self, alien):
        alien.sofrer_dano(1)
        if not alien.esta_vivo():
            self.pontuacao += 10

alien = Alien(0, 0, 3)
player = Jogador()
player.atacar(alien)
player.atacar(alien)
player.atacar(alien)
print(alien.vida)
print(alien.esta_vivo())
print(player.pontuacao)
""",
        'exemplos': """# Exemplo 1: Alienígena representado como dicionário
alien = {'x': 0, 'y': 1, 'vida': 2}
print(alien)

# Exemplo 2: Movimento
def mover(alien, dx, dy):
    alien['x'] += dx
    alien['y'] += dy

mover(alien, 1, 2)
print(alien)

# Exemplo 3: Ataque e pontos
pontuacao = 0
alien['vida'] -= 1
if alien['vida'] <= 0:
    pontuacao += 10
print(alien['vida'], pontuacao)

# Exemplo 4: Colisão
def colide(pos1, pos2):
    return pos1 == pos2
print(colide((1, 1), (1, 1)))
""",
    },
    '14': {
        'title': 'Pontuação e níveis',
        'explicacao': """# Pontuação e níveis

Este capítulo mostra como gerenciar a evolução do jogo com pontos e fases.

## Pontuação

A pontuação reflete o desempenho do jogador.

## Níveis

Cada nível pode ter regras ou dificuldade diferentes.

## Progressão

Suba de nível quando atingir metas de pontos.

## Dificuldade

Aumente a dificuldade com mais inimigos ou objetivos mais exigentes.

## Feedback

Mostre pontuação atual e metas para o próximo nível.
""",
        'codigos': """pontuacao = 0
nivel = 1
for i in range(1, 6):
    pontuacao += i * 10
    if pontuacao >= nivel * 50:
        nivel += 1
melhor = max(pontuacao, 80)
print('Pontuação:', pontuacao)
print('Nível atual:', nivel)
print('Recorde:', melhor)
""",
        'exemplos': """# Exemplo 1: Atualizar pontos
pontuacao = 0
pontuacao += 10
pontuacao += 20
print(pontuacao)

# Exemplo 2: Verificar nível
nivel = 1
if pontuacao >= 50:
    nivel += 1
print(nivel)

# Exemplo 3: Dificuldade
inimigos = nivel * 3
print('Inimigos:', inimigos)

# Exemplo 4: Próxima meta
meta = nivel * 100
print('Meta:', meta)
""",
    },
    '15': {
        'title': 'Simulações e gráficos',
        'explicacao': """# Simulações e gráficos

Este capítulo mostra como representar dados e fenômenos por meio de cálculos.

## Simulação

Simular significa calcular o comportamento de algo ao longo do tempo.

## Trajetórias

A física usa equações para descrever movimento e queda livre.

## Gráfico

Dados podem ser preparados em pares (x, y) para visualização.

## Ferramentas

Matplotlib é a biblioteca padrão para gráficos em Python, embora não seja usada neste capítulo.

## Aplicações

Simulação é útil em jogos, processos físicos e previsão de resultados.
""",
        'codigos': """import math

trajetoria = []
for t in range(0, 11):
    x = t
    y = 10 + 5 * t - 0.5 * 9.8 * t ** 2
    trajetoria.append((x, y))
valores = [math.sin(x / 10) for x in range(0, 31)]
print('Trajetória:', trajetoria)
print('Senoides:', valores)
""",
        'exemplos': """# Exemplo 1: Queda livre
for tempo in range(0, 6):
    altura = 100 - 4.9 * tempo ** 2
    print('tempo', tempo, 'altura', altura)

# Exemplo 2: Movimento linear
for passo in range(5):
    posicao = passo * 2
    print(posicao)

# Exemplo 3: Valores trigonométricos
import math
valores = [math.sin(math.radians(angulo)) for angulo in range(0, 181, 30)]
print(valores)

# Exemplo 4: Dados para gráfico
dados = [(x, x ** 2) for x in range(6)]
print(dados)
""",
    },
    '16': {
        'title': 'Dados e CSV',
        'explicacao': """# Dados e CSV

Este capítulo apresenta formatos tabulares e como processá-los em Python.

## CSV

CSV salva dados em texto, usando vírgulas para separar campos.

## Leitura e escrita

Use o módulo `csv` para trabalhar com arquivos CSV de forma estruturada.

## Dicionários

`csv.DictReader` e `csv.DictWriter` facilitam o uso de registros como dicionários.

## Conversão

Dados lidos de CSV são strings. Converta para `int`, `float` ou outros tipos quando necessário.

## Processamento

Filtre registros, calcule médias e extraia colunas.
""",
        'codigos': """import csv

dados = [
    {'nome': 'Ana', 'idade': '23'},
    {'nome': 'Bruno', 'idade': '28'},
]
with open('dados.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'idade'])
    escritor.writeheader()
    escritor.writerows(dados)

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    nomes = [linha['nome'] for linha in leitor]
print(nomes)
""",
        'exemplos': """# Exemplo 1: Escrever CSV
import csv
registros = [
    {'nome': 'Carlos', 'idade': '32'},
    {'nome': 'Lívia', 'idade': '27'},
]
with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'idade'])
    escritor.writeheader()
    escritor.writerows(registros)

# Exemplo 2: Ler CSV
with open('usuarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['nome'], linha['idade'])

# Exemplo 3: Filtrar
usuarios = [
    {'nome': 'Ana', 'idade': 23},
    {'nome': 'Bruno', 'idade': 18},
]
adultos = [u for u in usuarios if u['idade'] >= 18]
print(adultos)
""",
    },
    '17': {
        'title': 'APIs e JSON',
        'explicacao': """# APIs e JSON

Este capítulo apresenta como usar dados em JSON e se preparar para APIs.

## JSON

JSON é um formato de texto usado para representar estruturas de dados.

## Serialização e desserialização

- `json.dumps()` transforma dicionário em texto JSON.
- `json.loads()` converte texto JSON em dicionário.

## Estrutura de dados

JSON usa objetos e listas aninhadas para representar informações.

## APIs

APIs podem retornar JSON em respostas HTTP, permitindo integração entre sistemas.

## Prática

Extraia valores, trate erros e converta dados conforme necessário.
""",
        'codigos': """import json

texto = '{"nome": "Ana", "idade": 30}'
dados = json.loads(texto)
dados['cidade'] = 'Porto Alegre'
saida = json.dumps(dados, ensure_ascii=False)
print(dados)
print(saida)
""",
        'exemplos': """# Exemplo 1: JSON para dicionário
import json
json_texto = '{"nome": "João", "cidade": "São Paulo"}'
usuario = json.loads(json_texto)
print(usuario['nome'])

# Exemplo 2: Dicionário para JSON
dados = {'nome': 'Mariana', 'idade': 29}
json_texto = json.dumps(dados, ensure_ascii=False)
print(json_texto)

# Exemplo 3: Resposta de API simulada
resposta = {
    'status': 'ok',
    'dados': [
        {'id': 1, 'valor': 100},
        {'id': 2, 'valor': 200},
    ]
}
for item in resposta['dados']:
    print(item['id'], item['valor'])
""",
    },
    '18': {
        'title': 'Aplicativos e páginas',
        'explicacao': """# Aplicativos e páginas

Este capítulo mostra como Python pode gerar conteúdo e estruturar aplicações.

## Aplicativos

Aplicativos podem ser de linha de comando, web ou desktop.

## Páginas

Páginas HTML podem ser geradas a partir de strings de texto.

## Servidor simples

O módulo `http.server` cria um servidor local básico.

## Estrutura de código

Separe lógica de geração de conteúdo e apresentação.

## Utilidade

Mesmo um aplicativo simples deve ter funções claras e dados organizados.
""",
        'codigos': """from http.server import SimpleHTTPRequestHandler, HTTPServer

class Servidor(SimpleHTTPRequestHandler):
    pass

porta = 8000
httpd = HTTPServer(('localhost', porta), Servidor)
print(f'Servidor rodando em http://localhost:{porta}')
""",
        'exemplos': """# Exemplo 1: Gerar HTML
titulo = 'Minha página'
conteudo = '<p>Esta página foi gerada em Python.</p>'
html = f'<html><head><title>{titulo}</title></head><body>{conteudo}</body></html>'
print(html)

# Exemplo 2: Aplicativo simples
class Aplicativo:
    def __init__(self, nome):
        self.nome = nome

    def iniciar(self):
        print(f'Aplicativo {self.nome} iniciado')

app = Aplicativo('MeuApp')
app.iniciar()

# Exemplo 3: Dados para página
titulo = 'Página de Exemplo'
texto = 'Conteúdo gerado dinamicamente'
pagina = f'<h1>{titulo}</h1><p>{texto}</p>'
print(pagina)
""",
    },
    '19': {
        'title': 'Usuários e dados',
        'explicacao': """# Usuários e dados

Este capítulo ensina a organizar informações de usuários.

## Dados de usuários

Armazene nome, email, idade e outros dados em dicionários.

## Listas de registros

Agrupe usuários em listas para processar coleções.

## Filtragem

Use `for` e compreensões para buscar e filtrar dados.

## Validação

Verifique se campos existem antes de usá-los.

## Exportação

Dados de usuários podem ser gravados em arquivos CSV ou JSON.
""",
        'codigos': """usuarios = [
    {'nome': 'Alice', 'email': 'alice@example.com', 'idade': 24},
    {'nome': 'Bruno', 'email': 'bruno@example.com', 'idade': 30},
]
usuario_novo = {'nome': 'Carlos', 'email': 'carlos@example.com', 'idade': 27}
usuarios.append(usuario_novo)
emails = [usuario['email'] for usuario in usuarios]
adultos = [usuario for usuario in usuarios if usuario['idade'] >= 18]
print(usuarios)
print(emails)
print(adultos)
""",
        'exemplos': """# Exemplo 1: Lista de usuários
usuarios = [
    {'nome': 'Lucia', 'idade': 35},
    {'nome': 'Pedro', 'idade': 42},
]
print(usuarios)

# Exemplo 2: Adicionar usuário
novo_usuario = {'nome': 'Fernanda', 'idade': 28}
usuarios.append(novo_usuario)
print(usuarios)

# Exemplo 3: Buscar usuário
for usuario in usuarios:
    if usuario['nome'] == 'Pedro':
        print('Encontrado', usuario)

# Exemplo 4: Filtrar maiores de idade
adultos = [u for u in usuarios if u['idade'] >= 18]
print(adultos)
""",
    },
    '20': {
        'title': 'Diário de aprendizado',
        'explicacao': """# Diário de aprendizado

Este capítulo mostra como documentar o progresso e registrar anotações.

## Propósito do diário

Registrar aprendizado ajuda a fixar conhecimento e revisar o que foi absorvido.

## Estrutura de uma entrada

Uma entrada pode ter data, texto e tópicos estudados.

## Datas e horas

Use `datetime` para obter carimbo de data e hora e gerar registro confiável.

## Salvando em arquivo

Armazene entradas em texto, CSV ou JSON para leitura posterior.

## Revisão

Ler registros antigos mostra evolução e ajuda a planejar os próximos passos.
""",
        'codigos': """from datetime import datetime

def criar_entrada(texto):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'{agora} - {texto}'

entrada = criar_entrada('Hoje estudei Python e organizei o projeto.')
with open('diario.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(entrada + '\n')

with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
""",
        'exemplos': """# Exemplo 1: Criar anotação
from datetime import datetime
entrada = f'{datetime.now().date()} - Estudei variáveis'
print(entrada)

# Exemplo 2: Salvar em arquivo
with open('aprendizado.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(entrada + '\n')

# Exemplo 3: Ler histórico
topico = 'Python'
with open('aprendizado.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        if topico in linha:
            print(linha.strip())
""",
    },
    '21': {
        'title': 'Python profissional',
        'explicacao': """# Python profissional

Neste capítulo você aprende práticas para tornar o código mais profissional.

## Organização de projetos

Use pastas, módulos e nomes claros para facilitar manutenção.

## Biblioteca padrão

Python traz módulos como `pathlib`, `sqlite3`, `json`, `csv` e `datetime`.

## Expressões geradoras

Geradores criam valores sob demanda sem armazenar toda a sequência.

## Decoradores

Decoradores alteram o comportamento de funções de forma reutilizável.

## Bons hábitos

Documente código, use Nomes claros e mantenha funções pequenas.
""",
        'codigos': """from pathlib import Path
import sqlite3

caminho = Path('dados.db')
conn = sqlite3.connect(caminho)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, idade INTEGER)')
cursor.execute('INSERT INTO pessoas VALUES (?, ?)', ('Ana', 30))
conn.commit()
for row in cursor.execute('SELECT nome, idade FROM pessoas'):
    print(row)
conn.close()
""",
        'exemplos': """# Exemplo 1: Pathlib
from pathlib import Path
arquivo = Path('arquivo.txt')
print(arquivo.exists())
print(arquivo.stem)

# Exemplo 2: Generator expression
quadrados = (n * n for n in range(5))
for valor in quadrados:
    print(valor)

# Exemplo 3: Decorador simples
def mostrar_nome(func):
    def wrapper(*args, **kwargs):
        print('Executando função')
        return func(*args, **kwargs)
    return wrapper

@mostrar_nome
def diga_oi():
    print('Oi')

diga_oi()
""",
    },
}

target_files = {'explicacao.qmd', 'codigos.py', 'exemplos.py'}

for child in root.iterdir():
    if child.is_dir() and child.name.startswith('Capitulo'):
        chapter_number = child.name.split()[1]
        for item in list(child.iterdir()):
            if item.is_dir():
                shutil.rmtree(item)
            elif item.name not in target_files:
                item.unlink()
        content = chapters.get(chapter_number)
        if content is None:
            content = {
                'explicacao': f'# {child.name}\n\nConteúdo completo ainda não definido.',
                'codigos': 'print("Conteúdo não definido")\n',
                'exemplos': '# Exemplo não definido\n',
            }
        (child / 'explicacao.qmd').write_text(content['explicacao'], encoding='utf-8')
        (child / 'codigos.py').write_text(content['codigos'], encoding='utf-8')
        (child / 'exemplos.py').write_text(content['exemplos'], encoding='utf-8')
print('Todos os capítulos foram atualizados com conteúdo mais amplo e completo.')
