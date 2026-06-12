from pathlib import Path
from urllib.parse import quote
import unicodedata

root = Path('c:/Users/davidsantos/Documents/GitHub/Python-Basico')

chapters = {
    'Fundamentos básicos': [
        {
            'heading': 'O que são fundamentos básicos?',
            'content': 'Fundamentos básicos são o ponto de partida para aprender Python. Eles envolvem conceitos simples como variáveis, tipos, operadores e execução de código.',
            'bullets': [
                'Python é uma linguagem interpretada e de alto nível.',
                'O arquivo de código deve ter extensão .py.',
                'A indentação define blocos em Python.',
            ],
            'code': ['print("Olá, Python!")', 'idade = 25', 'print(idade)'],
            'note': 'Comece com exemplos curtos e teste no terminal para entender o comportamento do código.'
        },
        {
            'heading': 'Variáveis e tipos de dados',
            'content': 'Variáveis são nomes que armazenam valores. Python identifica o tipo automaticamente, sem necessidade de declaração prévia.',
            'bullets': [
                'int: números inteiros, como 10 ou -3.',
                'float: números decimais, como 2.5.',
                'str: textos entre aspas.',
                'bool: True ou False.',
            ],
            'code': ['nome = "Maria"', 'idade = 25', 'altura = 1.68', 'ativo = True', 'print(type(nome))'],
            'note': 'Use nomes descritivos e evite caracteres especiais. Substitua espaços por underscore (_).'
        },
        {
            'heading': 'Entrada e saída de dados',
            'content': 'A entrada de dados permite interagir com o usuário. A saída exibe resultados no terminal.',
            'bullets': [
                'input() lê texto do usuário.',
                'print() mostra valores na tela.',
                'input() sempre retorna string.',
                'Converta input() para int ou float quando necessário.',
            ],
            'code': ['nome = input("Digite seu nome: ")', 'idade = int(input("Digite sua idade: "))', 'print("Nome:", nome)', 'print("Idade:", idade)'],
            'note': 'Ao receber dados do usuário, valide o tipo antes de usar em cálculos.'
        },
    ],
    'Strings e variáveis': [
        {
            'heading': 'O que são strings?',
            'content': 'Strings são sequências de caracteres usadas para representar texto. Em Python, podem ser delimitadas por aspas simples, duplas ou triplas.',
            'bullets': [
                'Aspas simples: \'texto\'',
                'Aspas duplas: "texto"',
                'Aspas triplas para textos longos ou multilinhas.',
                'Strings são imutáveis.',
            ],
            'code': ['texto = "Olá, mundo"', 'print(texto)', 'print(texto[0])', 'print(texto[-1])'],
            'note': 'Use f-strings para formatar texto de forma legível e eficiente.'
        },
        {
            'heading': 'Como funcionam as variáveis',
            'content': 'Variáveis armazenam dados em memória e o Python determina o tipo com base no valor atribuído.',
            'bullets': [
                'Uma variável pode receber valores diferentes ao longo do tempo.',
                'Não é preciso declarar o tipo antes.',
                'O nome deve começar com letra ou underscore.',
            ],
            'code': ['nome = "João"', 'idade = 28', 'nome = "Maria"', 'print(nome, idade)'],
            'note': 'Prefira nomes como nome_aluno, preco_produto e total_venda.'
        },
        {
            'heading': 'Métodos úteis de string',
            'content': 'Strings têm vários métodos para manipular texto, como strip, replace, split e upper.',
            'bullets': [
                'strip() remove espaços nas extremidades.',
                'replace() substitui partes da string.',
                'split() divide o texto em uma lista.',
                'upper() e lower() alteram a capitalização.',
            ],
            'code': ['frase = "  Python é legal  "', 'print(frase.strip())', 'print(frase.replace("legal", "incrível"))', 'print(frase.upper())'],
            'note': 'Use métodos de string para limpar e formatar dados antes de exibi-los.'
        },
    ],
    'Listas': [
        {
            'heading': 'O que são listas?',
            'content': 'Listas são coleções ordenadas de valores. Elas podem conter diferentes tipos de dados e permitem adicionar, remover e acessar itens por índice.',
            'bullets': [
                'A primeira posição é o índice 0.',
                'Listas podem conter números, strings e até outras listas.',
                'Operações comuns incluem append, remove e pop.',
            ],
            'code': ['cores = ["vermelho", "verde", "azul"]', 'print(cores[0])', 'print(cores[-1])'],
            'note': 'Use listas quando a ordem importar e você precisar de coleções mutáveis.'
        },
        {
            'heading': 'Operações básicas em listas',
            'content': 'Você pode inserir itens, ordenar a lista, contar elementos e copiar listas.',
            'bullets': [
                'append() adiciona ao final.',
                'insert() insere em posição especificada.',
                'sort() ordena em ordem crescente.',
                'pop() remove e retorna um item.',
            ],
            'code': ['frutas = ["maçã", "banana"]', 'frutas.append("uva")', 'frutas.insert(1, "laranja")', 'print(frutas)'],
            'note': 'Evite modificar uma lista enquanto a percorre; use cópias quando necessário.'
        },
        {
            'heading': 'Compreensões de lista',
            'content': 'Compreensões permitem criar novas listas de forma concisa e elegante, usando uma expressão dentro de colchetes.',
            'bullets': [
                'São úteis para transformar ou filtrar dados.',
                'Podem substituir loops for simples.',
                'Tornam o código mais compacto.',
            ],
            'code': ['numeros = [1, 2, 3, 4, 5]', 'pares = [n for n in numeros if n % 2 == 0]', 'quadrados = [n*n for n in numeros]', 'print(pares, quadrados)'],
            'note': 'Prefira compreensões curtas; estruturas muito complexas podem prejudicar a legibilidade.'
        },
    ],
    'Laços e operações numéricas': [
        {
            'heading': 'O que são laços?',
            'content': 'Laços permitem repetir ações. Em Python, o for percorre elementos e o while repete enquanto a condição for verdadeira.',
            'bullets': [
                'for é ideal para listas, strings e range.',
                'while é útil quando o número de repetições não é conhecido.',
                'break e continue controlam o fluxo dentro do laço.',
            ],
            'code': ['for i in range(1, 6):', '    print(i)', 'n = 1', 'while n <= 3:', '    print(n)', '    n += 1'],
            'note': 'Evite loops infinitos garantindo que a condição do while mude ao longo do tempo.'
        },
        {
            'heading': 'Operadores numéricos',
            'content': 'Python oferece operadores como +, -, *, /, //, % e **. Eles permitem somar, subtrair, multiplicar e trabalhar com potências.',
            'bullets': [
                '/ retorna float.',
                '// retorna divisão inteira.',
                '% retorna o resto da divisão.',
                '** calcula potência.',
            ],
            'code': ['a = 7', 'b = 2', 'print(a + b)', 'print(a // b)', 'print(a % b)', 'print(a ** b)'],
            'note': 'Use parênteses para deixar clara a ordem das operações em expressões maiores.'
        },
        {
            'heading': 'Aplicações práticas',
            'content': 'Cálculos em loops são úteis para somar valores, contar itens e gerar séries numéricas.',
            'bullets': [
                'Acumular uma soma em um loop.',
                'Contar valores pares ou ímpares.',
                'Gerar tabelas de multiplicação.',
            ],
            'code': ['for i in range(1, 6):', '    print(f"{i} x 2 = {i * 2}")'],
            'note': 'Teste programas simples para familiarizar-se com operações e laços juntos.'
        },
    ],
    'Condicionais': [
        {
            'heading': 'O que são condicionais?',
            'content': 'Condicionais escolhem entre caminhos diferentes no programa. if, elif e else permitem reagir aos valores e às entradas do usuário.',
            'bullets': [
                'if verifica uma condição.',
                'elif adiciona verificações extras.',
                'else trata o caso padrão.',
            ],
            'code': ['idade = int(input("Digite a idade: "))', 'if idade >= 18:', '    print("Maior de idade")', 'else:', '    print("Menor de idade")'],
            'note': 'Escreva condições na ordem mais provável para melhorar a eficiência.'
        },
        {
            'heading': 'Operadores lógicos',
            'content': 'and, or e not combinam condições e permitem criar verificações mais complexas.',
            'bullets': [
                'and exige todas verdadeiras.',
                'or exige pelo menos uma verdadeira.',
                'not inverte o resultado lógico.',
            ],
            'code': ['tem_ingresso = True', 'idade = 16', 'if tem_ingresso and idade >= 18:', '    print("Entrada liberada")', 'else:', '    print("Entrada negada")'],
            'note': 'Use parênteses para deixar claro o agrupamento de condições.'
        },
        {
            'heading': 'Boas práticas com condicionais',
            'content': 'Mantenha as condições simples e legíveis. Evite aninhar muitos ifs e prefira declarar variáveis auxiliares quando necessário.',
            'bullets': [
                'Prefira if/elif/else a múltiplos if independentes.',
                'Use nomes claros para condições booleanas.',
                'Evite expressões muito longas na mesma linha.',
            ],
            'code': ['idade = 20', 'aprovado = True', 'if idade >= 18 and aprovado:', '    print("Acesso permitido")'],
            'note': 'Separar condições complexas em variáveis nomeadas torna o código mais fácil de entender.'
        },
    ],
    'Dicionários e coleções': [
        {
            'heading': 'O que são dicionários?',
            'content': 'Dicionários armazenam pares chave:valor. Eles são ótimos para representar registros e buscar valores por chave.',
            'bullets': [
                'As chaves podem ser strings, números ou tuplas.',
                'Os valores podem ser qualquer tipo Python.',
                'Acesso é feito por usuario["nome"].',
            ],
            'code': ['usuario = {"nome": "Ana", "idade": 25}', 'print(usuario["nome"])', 'usuario["cidade"] = "SP"'],
            'note': 'Use get() para acessar chaves que podem não existir e evitar erros.'
        },
        {
            'heading': 'Tuplas e conjuntos',
            'content': 'Tuplas são listas imutáveis. Conjuntos armazenam valores únicos e suportam operações como união e interseção.',
            'bullets': [
                'Tuplas são criadas com parênteses.',
                'Conjuntos são criados com chaves ou set().',
                'Sets não mantêm ordem fixa.',
            ],
            'code': ['coords = (10, 20)', 'unicos = {1, 2, 2, 3}', 'print(unicos)'],
            'note': 'Use tuplas quando a sequência não deve mudar e conjuntos para eliminar duplicatas.'
        },
        {
            'heading': 'Métodos úteis',
            'content': 'Os dicionários têm métodos como keys, values e items. Esses métodos ajudam a iterar e transformar dados com facilidade.',
            'bullets': [
                'keys() retorna as chaves.',
                'values() retorna os valores.',
                'items() retorna pares (chave, valor).',
            ],
            'code': ['for chave, valor in usuario.items():', '    print(chave, valor)'],
            'note': 'Iterar sobre items() é útil para processar o conteúdo completo de um dicionário.'
        },
    ],
    'Loops e controle de fluxo': [
        {
            'heading': 'O que são loops?',
            'content': 'Loops repetem blocos de código. Eles são essenciais para processar coleções e repetir tarefas até que uma condição seja satisfeita.',
            'bullets': [
                'for itera sobre sequências.',
                'while repete com base em condição.',
                'loops ajudam a reduzir código repetido.',
            ],
            'code': ['nomes = ["Ana", "Bruno", "Carla"]', 'for nome in nomes:', '    print(nome)'],
            'note': 'Prefira for quando você já sabe os elementos a serem percorridos.'
        },
        {
            'heading': 'Break e continue',
            'content': 'break encerra o loop imediatamente. continue pula o restante da iteração e passa à próxima volta.',
            'bullets': [
                'break é útil para sair cedo.',
                'continue evita executar código adicional na mesma volta.',
                'else no loop executa se não houver break.',
            ],
            'code': ['for n in range(1, 6):', '    if n == 3:', '        continue', '    if n == 5:', '        break', '    print(n)'],
            'note': 'Use esses comandos com moderação para não tornar o fluxo confuso.'
        },
        {
            'heading': 'Enumerate e índices',
            'content': 'enumerate() fornece o índice e o valor ao iterar, tornando mais claro quando você precisa do número da posição.',
            'bullets': [
                'Permite acessar o índice sem contadores manuais.',
                'Facilita criar saídas numeradas.',
                'Funciona com strings e listas.',
            ],
            'code': ['cores = ["vermelho", "verde"]', 'for i, cor in enumerate(cores, 1):', '    print(i, cor)'],
            'note': 'Use enumerate sempre que precisar da posição do elemento durante a iteração.'
        },
    ],
    'Funções e módulos': [
        {
            'heading': 'O que são funções?',
            'content': 'Funções agrupam instruções em blocos reutilizáveis. Elas recebem parâmetros e podem retornar valores.',
            'bullets': [
                'Defina funções com def.',
                'Use return para devolver resultados.',
                'Funções tornam o código mais organizado.',
            ],
            'code': ['def soma(a, b):', '    return a + b', 'print(soma(3, 5))'],
            'note': 'Dê nomes claros às funções para indicar o que elas fazem.'
        },
        {
            'heading': 'Módulos e importações',
            'content': 'Módulos permitem dividir o código em arquivos. Importe funcionalidades com import ou from ... import ...',
            'bullets': [
                'import math',
                'from datetime import datetime',
                'Evite duplicar código em vários arquivos.',
            ],
            'code': ['import math', 'print(math.sqrt(16))'],
            'note': 'Separe funções relacionadas em módulos temáticos para facilitar o reuso.'
        },
        {
            'heading': 'Parâmetros padrão',
            'content': 'Parâmetros padrão permitem chamar funções sem passar todos os argumentos. Eles tornam a função mais flexível.',
            'bullets': [
                'def saudacao(nome="visitante"):',
                'Parâmetros padrão são usados quando o valor não é fornecido.',
                'Permitem evitar checagens manuais dentro da função.',
            ],
            'code': ['def saudacao(nome="visitante"):', '    return f"Olá, {nome}!"', 'print(saudacao())', 'print(saudacao("Ana"))'],
            'note': 'Use valores padrão que façam sentido para o contexto da função.'
        },
    ],
    'Classes e objetos': [
        {
            'heading': 'O que são classes?',
            'content': 'Classes são templates para criar objetos. Elas descrevem quais atributos e métodos os objetos terão.',
            'bullets': [
                'Classe é como uma planta.',
                'Objeto é a instância criada a partir da classe.',
                'Atributos guardam estado.',
            ],
            'code': ['class Pessoa:', '    def __init__(self, nome, idade):', '        self.nome = nome', '        self.idade = idade', 'p = Pessoa("Luna", 22)', 'print(p.nome)'],
            'note': 'Use classes para agrupar dados e comportamentos relacionados.'
        },
        {
            'heading': 'Atributos e métodos',
            'content': 'Atributos são variáveis do objeto. Métodos são funções que operam sobre esses atributos.',
            'bullets': [
                'self referencia a própria instância.',
                'Métodos são chamados com ponto: obj.metodo()',
                'Construtor __init__ cria o objeto.',
            ],
            'code': ['class Carro:', '    def __init__(self, marca):', '        self.marca = marca', '    def descricao(self):', '        return f"Carro: {self.marca}"', 'c = Carro("Fiat")', 'print(c.descricao())'],
            'note': 'Mantenha métodos focados em uma única ação ou responsabilidade.'
        },
        {
            'heading': 'Herança e polimorfismo',
            'content': 'Herança permite criar classes derivadas que reutilizam código da classe base. Polimorfismo permite tratar objetos diferentes de forma similar.',
            'bullets': [
                'class Aluno(Pessoa):',
                'super() chama o construtor da classe pai.',
                'Métodos podem ser sobrescritos.',
            ],
            'code': ['class Pessoa:', '    def __init__(self, nome):', '        self.nome = nome', 'class Aluno(Pessoa):', '    pass', 'a = Aluno("João")', 'print(a.nome)'],
            'note': 'Use herança com moderação para evitar hierarquias complexas demais.'
        },
    ],
    'Arquivos e exceções': [
        {
            'heading': 'Como abrir arquivos',
            'content': 'Use open() para abrir arquivos. Os modos mais comuns são r, w, a e x.',
            'bullets': [
                'r: leitura',
                'w: escrita (sobrescreve)',
                'a: acrescentar',
                'x: criar somente se não existir',
            ],
            'code': ['with open("texto.txt", "w", encoding="utf-8") as f:', '    f.write("Olá\n")'],
            'note': 'Sempre especifique encoding="utf-8" para evitar problemas de caracteres.'
        },
        {
            'heading': 'Ler e gravar dados',
            'content': 'Você pode ler o arquivo inteiro com read() ou linha a linha com readline() e readlines().',
            'bullets': [
                'read() retorna todo o conteúdo.',
                'readline() lê uma linha por vez.',
                'readlines() retorna uma lista de linhas.',
            ],
            'code': ['with open("texto.txt", "r", encoding="utf-8") as f:', '    for linha in f:', '        print(linha.strip())'],
            'note': 'Prefira iterar diretamente sobre o arquivo em vez de usar readlines() para arquivos grandes.'
        },
        {
            'heading': 'Tratando exceções',
            'content': 'Use try e except para capturar erros e evitar que o programa pare de forma inesperada.',
            'bullets': [
                'try executa o bloco principal.',
                'except captura o erro.',
                'finally roda sempre, mesmo com erro.',
            ],
            'code': ['try:', '    with open("inexistente.txt", "r", encoding="utf-8") as f:', '        print(f.read())', 'except FileNotFoundError:', '    print("Arquivo não encontrado")'],
            'note': 'Trate apenas os erros que você espera, em vez de capturar exceções genéricas demais.'
        },
    ],
    'Funções e testes': [
        {
            'heading': 'Por que testar funções?',
            'content': 'Testar funções garante que elas retornem o resultado esperado. Isso evita regressões quando o código cresce.',
            'bullets': [
                'Testes ajudam a encontrar bugs cedo.',
                'asserts são ótimos para validações simples.',
                'Testes tornam o código mais confiável.',
            ],
            'code': ['def dobro(x):', '    return x * 2', 'assert dobro(3) == 6', 'print("Teste passou")'],
            'note': 'Use asserts durante o desenvolvimento para validar comportamentos críticos.'
        },
        {
            'heading': 'Testes básicos com assert',
            'content': 'assert verifica se uma condição é verdadeira. Se não for, ele lança uma AssertionError.',
            'bullets': [
                'assert condição',
                'Use mensagens de erro quando necessário.',
                'asserts são simples e diretos.',
            ],
            'code': ['def soma(a, b):', '    return a + b', 'assert soma(2, 3) == 5'],
            'note': 'Não use assert para controle de fluxo em produção; ele é uma ferramenta de testes.'
        },
        {
            'heading': 'Funções bem escritas',
            'content': 'Mantenha funções pequenas e com responsabilidade única. Cada função deve fazer uma tarefa clara.',
            'bullets': [
                'Evite funções muito longas.',
                'Use nomes que descrevam a ação.',
                'Separe lógica em funções auxiliares.',
            ],
            'code': ['def calcula_media(notas):', '    return sum(notas) / len(notas)', 'print(calcula_media([7, 8, 9]))'],
            'note': 'Funções bem projetadas tornam o código mais fácil de testar e manter.'
        },
    ],
    'Projeto de jogo': [
        {
            'heading': 'O que é este projeto?',
            'content': 'O projeto de jogo mostra como juntar variáveis, laços e condicionais para criar um pequeno jogo interativo.',
            'bullets': [
                'Inicializa estado do jogo.',
                'Recebe ações do jogador.',
                'Atualiza pontuação e vidas.',
            ],
            'code': ['vidas = 3', 'pontos = 0', 'print("Jogo iniciado")'],
            'note': 'Pense no jogo como um conjunto de estados que mudam ao longo de cada rodada.'
        },
        {
            'heading': 'Estrutura do jogo',
            'content': 'Um jogo simples tem três partes principais: inicialização, loop principal e verificação de fim de jogo.',
            'bullets': [
                'Inicie variáveis de pontuação e vidas.',
                'Use loop para repetir o jogo.',
                'Verifique condições de vitória ou derrota.',
            ],
            'code': ['while vidas > 0:', '    acao = input("Atacar ou fugir? ")', '    if acao == "atacar":', '        pontos += 10'],
            'note': 'Mantenha o loop principal claro, com uma condição de saída bem definida.'
        },
        {
            'heading': 'Pontuação e progresso',
            'content': 'A pontuação registra o desempenho do jogador. Subir de nível pode depender de metas de pontos.',
            'bullets': [
                'Use variáveis para guardar pontos e nível.',
                'Atualize o estado após cada ação.',
                'Mostre feedback ao jogador a cada rodada.',
            ],
            'code': ['pontos += 10', 'if pontos >= 50:', '    nivel += 1', '    print("Subiu de nível")'],
            'note': 'Decida regras simples para progressão antes de implementar o jogo.'
        },
    ],
    'Jogo com alienígenas': [
        {
            'heading': 'O que são alienígenas?',
            'content': 'Alienígenas são inimigos no jogo. Cada um pode ter posição, vida e comportamento. Eles podem ser modelados com dicionários ou classes.',
            'bullets': [
                'Cada alien tem vida e posição.',
                'O jogador pode atacar e reduzir a vida.',
                'Quando vida chega a zero, o alien é derrotado.',
            ],
            'code': ['alien = {"x": 0, "y": 1, "vida": 3}', 'print(alien)'],
            'note': 'Modelar inimigos com dicionários facilita adicionar propriedades e comportamentos.'
        },
        {
            'heading': 'Ataque e defesa',
            'content': 'O jogador realiza ações como atacar ou fugir. Essas ações alteram o estado do inimigo e do jogo.',
            'bullets': [
                'Ataque reduz a vida do inimigo.',
                'Cada inimigo pode dar pontos diferentes.',
                'Verifique se a vida ficou abaixo de zero.',
            ],
            'code': ['dano = 1', 'alien["vida"] -= dano', 'if alien["vida"] <= 0:', '    print("Alien derrotado")'],
            'note': 'Verifique os limites para evitar valores negativos de vida.'
        },
        {
            'heading': 'Atualização de estado',
            'content': 'A cada ciclo do jogo, atualize posição, vida e pontuação. Isso mantém o jogo dinâmico e previsível.',
            'bullets': [
                'Atualize inimigos e jogador a cada rodada.',
                'Use laços para repetir ações.',
                'Mostre o estado atual quando necessário.',
            ],
            'code': ['while alien["vida"] > 0:', '    print("O jogo continua")', '    break'],
            'note': 'Uma boa atualização de estado evita bugs e torna o jogo mais fácil de estender.'
        },
    ],
    'Pontuação e níveis': [
        {
            'heading': 'Como funciona a pontuação?',
            'content': 'Pontuação recompensa ações do jogador. Ela pode crescer ao completar objetivos ou derrotar inimigos.',
            'bullets': [
                'A pontuação é acumulativa.',
                'Diferentes ações podem dar valores diferentes.',
                'Use variáveis para rastrear o total.',
            ],
            'code': ['pontos = 0', 'pontos += 10', 'print(pontos)'],
            'note': 'Defina regras claras para pontuação antes de implementar o jogo.'
        },
        {
            'heading': 'Subindo de nível',
            'content': 'O nível indica progresso. Ele pode aumentar quando o jogador atinge uma meta de pontos.',
            'bullets': [
                'Meta de pontos para subir de nível.',
                'Níveis podem aumentar a dificuldade.',
                'Mostre qual falta para chegar ao próximo nível.',
            ],
            'code': ['nivel = 1', 'if pontos >= 50:', '    nivel += 1', '    print("Nível", nivel)'],
            'note': 'Níveis também podem desbloquear novas funcionalidades ou desafios.'
        },
        {
            'heading': 'Dificuldade e metas',
            'content': 'A dificuldade deve aumentar de forma equilibrada. Metas claras ajudam o jogador a entender o progresso.',
            'bullets': [
                'Aumente a dificuldade gradualmente.',
                'Use metas visíveis para orientar o jogador.',
                'Considere mais inimigos ou regras diferentes.',
            ],
            'code': ['meta = nivel * 50', 'print(f"Faltam {meta - pontos} pontos para subir")'],
            'note': 'Metas transparentes tornam o jogo mais justo e motivador.'
        },
    ],
    'Simulações e gráficos': [
        {
            'heading': 'O que é simulação?',
            'content': 'Simulação calcula o comportamento de um sistema ao longo do tempo. Em Python, usamos loops e fórmulas para gerar resultados passo a passo.',
            'bullets': [
                'Simular movimento, quedas ou crescimento.',
                'Guardar resultados em listas de dados.',
                'Visualizar o comportamento ao longo do tempo.',
            ],
            'code': ['for t in range(0, 6):', '    altura = 100 - 4.9 * t ** 2', '    print(t, altura)'],
            'note': 'Anote os valores em cada etapa para entender como a simulação evolui.'
        },
        {
            'heading': 'Dados para gráficos',
            'content': 'Dados de simulação podem ser organizados como pares x/y e usados para criar gráficos ou tabelas.',
            'bullets': [
                'Cada ponto tem posição e valor.',
                'Listas de tuplas facilitam o uso em bibliotecas de plotagem.',
                'Mesmo sem biblioteca, os dados são úteis para análise.',
            ],
            'code': ['dados = [(x, x ** 2) for x in range(6)]', 'print(dados)'],
            'note': 'Gráficos ajudam a ver tendências que não aparecem apenas pelo número bruto.'
        },
        {
            'heading': 'Cálculos comuns',
            'content': 'Funções matemáticas como seno, cosseno e raiz quadrada são comuns em simulações e podem ser usadas para criar movimento realista.',
            'bullets': [
                'Use math para funções trigonométricas.',
                'Equações simples descrevem movimento e trajetórias.',
                'A cada passo de tempo, recalculam-se posições.',
            ],
            'code': ['import math', 'for ang in range(0, 181, 30):', '    print(math.sin(math.radians(ang)))'],
            'note': 'Pequenas simulações são ótimas para aprender como a matemática se aplica a programas.'
        },
    ],
    'Dados e CSV': [
        {
            'heading': 'O que é CSV?',
            'content': 'CSV é um formato de texto para tabelas, onde cada linha representa um registro e as colunas são separadas por vírgulas.',
            'bullets': [
                'É amplamente usado para dados tabulares.',
                'Pode ser lido por planilhas e programas.',
                'É simples e legível por humanos.',
            ],
            'code': ['import csv', 'dados = [["nome", "idade"], ["Ana", "23"]]'],
            'note': 'Use CSV quando precisar trocar dados entre sistemas diferentes.'
        },
        {
            'heading': 'Lendo e escrevendo CSV',
            'content': 'Use csv.DictReader e csv.DictWriter para trabalhar com linhas como dicionários, o que torna o acesso aos campos mais claro.',
            'bullets': [
                'writeheader() grava o cabeçalho.',
                'DictReader lê cada linha como dicionário.',
                'Trate valores como strings e converta quando preciso.',
            ],
            'code': ['with open("dados.csv", "w", newline="", encoding="utf-8") as f:', '    escritor = csv.DictWriter(f, fieldnames=["nome", "idade"])', '    escritor.writeheader()', '    escritor.writerow({"nome": "Ana", "idade": "23"})'],
            'note': 'Sempre abra arquivos CSV com newline="" para evitar linhas em branco extras no Windows.'
        },
        {
            'heading': 'Convertendo tipos',
            'content': 'Quando você lê CSV, valores chegam como texto. Converta para int, float ou outros tipos antes de usar em cálculos.',
            'bullets': [
                'int() para inteiros.',
                'float() para decimais.',
                'bool() para valores booleanos quando necessário.',
            ],
            'code': ['idade = int(linha["idade"])', 'preco = float(linha["preco"])'],
            'note': 'Valide o conteúdo antes de converter para evitar ValueError.'
        },
    ],
    'APIs e JSON': [
        {
            'heading': 'O que é JSON?',
            'content': 'JSON é um formato de texto para representar dados estruturados de forma leve. Ele usa objetos e listas para organizar informações.',
            'bullets': [
                'Objetos são delimitados por chaves {}.',
                'Listas são delimitadas por colchetes [].',
                'Strings usam aspas duplas.',
            ],
            'code': ['import json', 'texto = "{\"nome\": \"Ana\", \"idade\": 30}"', 'dados = json.loads(texto)', 'print(dados)'],
            'note': 'JSON é muito usado em APIs e trocas de dados entre sistemas web.'
        },
        {
            'heading': 'Como usar JSON em Python',
            'content': 'Use json.loads() para converter texto JSON em dicionário Python e json.dumps() para gerar JSON a partir de dados Python.',
            'bullets': [
                'loads() transforma JSON em Python.',
                'dumps() transforma Python em JSON.',
                'indent facilita a leitura do JSON gerado.',
            ],
            'code': ['saida = json.dumps(dados, ensure_ascii=False, indent=2)', 'print(saida)'],
            'note': 'Use ensure_ascii=False para preservar caracteres acentuados no JSON.'
        },
        {
            'heading': 'APIs e integração',
            'content': 'APIs normalmente retornam JSON em respostas HTTP. Saber ler e interpretar esse JSON é essencial para integrar serviços.',
            'bullets': [
                'Respostas de API vêm como texto JSON.',
                'Extraia os campos necessários do objeto Python.',
                'Verifique o status da resposta antes de usar os dados.',
            ],
            'code': ['resposta = {"status": "ok", "dados": [{"id": 1}]}', 'print(resposta["dados"][0]["id"])'],
            'note': 'Mesmo sem fazer chamadas HTTP, praticar JSON prepara você para trabalhar com APIs reais.'
        },
    ],
    'Aplicativos e páginas': [
        {
            'heading': 'O que são aplicativos?',
            'content': 'Aplicativos podem ser programas de terminal, páginas HTML ou serviços web. Python é capaz de criar e controlar esses formatos.',
            'bullets': [
                'Aplicativos de linha de comando usam input e print.',
                'Páginas HTML podem ser geradas como texto.',
                'Servidores web entregam HTML a navegadores.',
            ],
            'code': ['titulo = "Minha página"', 'html = f"<h1>{titulo}</h1>"', 'print(html)'],
            'note': 'Mesmo sem servidor, gerar HTML em Python demonstra como páginas podem ser construídas dinamicamente.'
        },
        {
            'heading': 'Gerando páginas HTML',
            'content': 'HTML pode ser montado como string em Python. Com isso, você consegue criar conteúdo estático ou dinâmico facilmente.',
            'bullets': [
                'Use strings multilinha para HTML.',
                'Insira dados com f-strings.',
                'Salve em arquivo .html para abrir no navegador.',
            ],
            'code': ['html = """<html><body><h1>Olá</h1></body></html>"""', 'with open("pagina.html", "w", encoding="utf-8") as f:', '    f.write(html)'],
            'note': 'Mantenha o HTML simples no início antes de evoluir para estruturas mais complexas.'
        },
        {
            'heading': 'Servidores simples',
            'content': 'O módulo http.server permite criar um servidor local básico para servir páginas HTML durante testes.',
            'bullets': [
                'Use HTTPServer e BaseHTTPRequestHandler.',
                'É útil para protótipos e demonstrações.',
                'Não é indicado para produção.',
            ],
            'code': ['from http.server import BaseHTTPRequestHandler, HTTPServer', 'print("Servidor local pronto")'],
            'note': 'Esse servidor é ideal para testar páginas estáticas localmente.'
        },
    ],
    'Usuários e dados': [
        {
            'heading': 'Organizando informações de usuários',
            'content': 'Dados de usuários podem ser armazenados em listas de dicionários. Assim, é possível buscar e filtrar informações com facilidade.',
            'bullets': [
                'Cada usuário pode ser um dicionário.',
                'Listas agrupam vários registros.',
                'Acesso é feito por chave.',
            ],
            'code': ['usuarios = [{"nome": "Ana", "idade": 24}]', 'print(usuarios[0]["nome"])'],
            'note': 'Mantenha o formato consistente para facilitar a manipulação dos dados.'
        },
        {
            'heading': 'Filtrando e buscando',
            'content': 'Use loops e compreensões para encontrar usuários que atendam a critérios específicos, como idade ou cidade.',
            'bullets': [
                'Filtre com if dentro de loops.',
                'Compreensões simplificam a sintaxe.',
                'Resultados podem ser usados em relatórios ou exibições.',
            ],
            'code': ['adultos = [u for u in usuarios if u["idade"] >= 18]', 'print(adultos)'],
            'note': 'Valide campos antes de usá-los para evitar KeyError.'
        },
        {
            'heading': 'Validando dados',
            'content': 'Verifique se os campos existem e se os valores estão no formato esperado antes de usar os dados em cálculos ou exibições.',
            'bullets': [
                'Use in para checar chaves.',
                'Converta tipos quando necessário.',
                'Trate valores faltantes com valores padrão.',
            ],
            'code': ['if "email" in usuario:', '    print(usuario["email"])'],
            'note': 'Dados bem validados tornam seu programa mais robusto e menos sujeito a erros.'
        },
    ],
    'Diário de aprendizado': [
        {
            'heading': 'Por que manter um diário?',
            'content': 'Um diário de aprendizado permite registrar progresso, dúvidas e descobertas. Ele é útil para revisão e motivação.',
            'bullets': [
                'Registra o que foi estudado.',
                'Permite revisar o conteúdo depois.',
                'Ajuda a planejar os próximos passos.',
            ],
            'code': ['from datetime import datetime', 'entrada = f"{datetime.now().date()} - Estudei Python"', 'print(entrada)'],
            'note': 'Anotar pequenos detalhes ajuda a consolidar o aprendizado.'
        },
        {
            'heading': 'Estrutura de uma entrada',
            'content': 'Uma boa entrada tem data, tópico, descrição do que foi feito e observações sobre dificuldades ou pontos importantes.',
            'bullets': [
                'Data e hora do registro.',
                'Tópico estudado.',
                'Resumo do que aprendeu.',
            ],
            'code': ['entrada = "2026-06-12 - Estudei laços em Python"', 'print(entrada)'],
            'note': 'Use um formato consistente para facilitar buscas no diário.'
        },
        {
            'heading': 'Salvando em arquivo',
            'content': 'Armazene as entradas em arquivos de texto ou CSV para consultar o histórico sempre que precisar.',
            'bullets': [
                'Use append para adicionar novas entradas.',
                'Leia o arquivo para revisar o histórico.',
                'Mantenha o conteúdo legível.',
            ],
            'code': ['with open("diario.txt", "a", encoding="utf-8") as f:', '    f.write(entrada + "\n")'],
            'note': 'Salve o diário em formato simples para poder abrir em qualquer editor.'
        },
    ],
    'Python profissional': [
        {
            'heading': 'O que significa Python profissional?',
            'content': 'Python profissional envolve escrever código legível, organizado e reutilizável. Também inclui pensar em manutenção e clareza para outras pessoas.',
            'bullets': [
                'Use nomes claros e consistentes.',
                'Separe responsabilidades em funções e módulos.',
                'Documente o código quando necessário.',
            ],
            'code': ['from pathlib import Path', 'arquivo = Path("dados.txt")', 'print(arquivo.exists())'],
            'note': 'Código limpo é tão importante quanto código que funciona.'
        },
        {
            'heading': 'Ferramentas da biblioteca padrão',
            'content': 'Python traz módulos úteis como pathlib, datetime, json e csv. Eles ajudam a resolver tarefas comuns sem instalar pacotes extras.',
            'bullets': [
                'pathlib para caminhos de arquivo.',
                'datetime para datas e horas.',
                'json e csv para dados estruturados.',
            ],
            'code': ['from datetime import datetime', 'print(datetime.now())'],
            'note': 'Conhecer a biblioteca padrão aumenta sua produtividade como desenvolvedor.'
        },
        {
            'heading': 'Boas práticas de código',
            'content': 'Mantenha funções pequenas, evite duplicação e prefira código simples. Esses hábitos tornam o projeto mais fácil de manter no longo prazo.',
            'bullets': [
                'Evite funções muito longas.',
                'Use comentários apenas quando necessário.',
                'Refatore código repetido em funções.',
            ],
            'code': ['def salvar_texto(arquivo, conteudo):', '    with open(arquivo, "w", encoding="utf-8") as f:', '        f.write(conteudo)'],
            'note': 'Pequenas melhorias constantes tornam seu estilo de programação mais profissional.'
        },
    ],
}

final_examples = {
    'Fundamentos básicos': ['nome = input("Qual seu nome? ")', 'idade = int(input("Qual sua idade? "))', 'altura = float(input("Qual sua altura? "))', 'print("Nome:", nome)', 'print("Idade:", idade)', 'print("Altura:", altura)'],
    'Strings e variáveis': ['nome = input("Qual seu nome? ")', 'sobrenome = input("Qual seu sobrenome? ")', 'nome_completo = nome + " " + sobrenome', 'print("Nome completo:", nome_completo)'],
    'Listas': ['frutas = ["maçã", "banana", "uva"]', 'for fruta in frutas:', '    print(fruta)'],
    'Laços e operações numéricas': ['for n in range(1, 6):', '    print(n, n * n)'],
    'Condicionais': ['idade = int(input("Digite sua idade: "))', 'if idade >= 18:', '    print("Maior de idade")', 'else:', '    print("Menor de idade")'],
    'Dicionários e coleções': ['usuario = {"nome": "Ana", "idade": 24}', 'print(usuario["nome"])'],
    'Loops e controle de fluxo': ['for i in range(1, 6):', '    if i % 2 == 0:', '        print(i, "é par")'],
    'Funções e módulos': ['def soma(a, b=0):', '    return a + b', 'print(soma(3, 4))'],
    'Classes e objetos': ['class Pessoa:', '    def __init__(self, nome, idade):', '        self.nome = nome', '        self.idade = idade', 'p = Pessoa("João", 30)', 'print(p.nome)'],
    'Arquivos e exceções': ['with open("saida.txt", "w", encoding="utf-8") as f:', '    f.write("Teste\n")', 'with open("saida.txt", "r", encoding="utf-8") as f:', '    print(f.read())'],
    'Funções e testes': ['def dobra(x):', '    return x * 2', 'assert dobra(4) == 8', 'print("TesteOK")'],
    'Projeto de jogo': ['vidas = 3', 'pontos = 0', 'print("Jogo iniciado com", vidas, "vidas")'],
    'Jogo com alienígenas': ['alien = {"vida": 3, "x": 0}', 'alien["vida"] -= 1', 'print("Vida do alien:", alien["vida"])'],
    'Pontuação e níveis': ['pontuacao = 40', 'nivel = 1', 'if pontuacao >= 50:', '    nivel += 1', 'print("Nível:", nivel)'],
    'Simulações e gráficos': ['import math', 'for t in range(6):', '    y = 10 + 5 * t - 4.9 * t ** 2', '    print(t, y)'],
    'Dados e CSV': ['import csv', 'with open("dados.csv", "w", newline="", encoding="utf-8") as f:', '    escritor = csv.writer(f)', '    escritor.writerow(["nome", "idade"])', '    escritor.writerow(["Ana", 23])'],
    'APIs e JSON': ['import json', 'dados = {"nome": "Ana", "idade": 30}', 'print(json.dumps(dados, ensure_ascii=False))'],
    'Aplicativos e páginas': ['html = "<h1>Minha página</h1>"', 'with open("pagina.html", "w", encoding="utf-8") as f:', '    f.write(html)'],
    'Usuários e dados': ['usuarios = [{"nome": "Bruno", "idade": 28}]', 'for u in usuarios:', '    print(u["nome"])'],
    'Diário de aprendizado': ['from datetime import datetime', 'entrada = f"{datetime.now().date()} - Estudei Python"', 'with open("diario.txt", "a", encoding="utf-8") as f:', '    f.write(entrada + "\n")'],
    'Python profissional': ['from pathlib import Path', 'p = Path("arquivo.txt")', 'print(p.exists())'],
}


def slugify(value: str) -> str:
    value = unicodedata.normalize('NFD', value)
    value = ''.join(ch for ch in value if unicodedata.category(ch) != 'Mn')
    value = value.lower()
    value = ''.join(ch if ch.isalnum() or ch.isspace() or ch == '-' else '' for ch in value)
    return '-'.join(value.split())


def chapter_url(path: Path) -> str:
    rel = path.relative_to(root).as_posix()
    return 'https://github.com/DavidKelvy/Python-Basico/blob/main/' + quote(rel)


def make_link(url: str, anchor: str) -> str:
    return f'[]({url}#{anchor})'


def build_text(title: str, qmd_path: Path) -> str:
    url = chapter_url(qmd_path)
    title_anchor = slugify(title)
    lines = [f'# {title}', make_link(url, title_anchor), '', '---', '']
    for section in chapters[title]:
        anchor = slugify(section['heading'])
        lines.append(f'## {section["heading"]}')
        lines.append(make_link(url, anchor))
        lines.append(section['content'])
        lines.append('')
        if section.get('bullets'):
            for item in section['bullets']:
                lines.append(f'- {item}')
            lines.append('')
        if section.get('note'):
            lines.append(f'> {section["note"]}')
            lines.append('')
        if section.get('code'):
            lines.append('```python')
            lines.extend(section['code'])
            lines.append('```')
            lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Exemplo Prático no VS Code')
    lines.append(make_link(url, f'{title_anchor}-exemplo-pratico-no-vs-code'))
    lines.append('1. Abra o VS Code e crie um arquivo chamado `exemplo.py`.')
    lines.append('2. Copie o código abaixo e salve o arquivo.')
    lines.append('3. Execute no terminal com `python exemplo.py`.')
    lines.append('')
    lines.append('```python')
    for line in final_examples.get(title, ['print("Exemplo prático de uso do capítulo")']):
        lines.append(line)
    lines.append('```')
    return '\n'.join(lines)

for chapter_dir in sorted(root.glob('Capitulo *')):
    qmd_path = chapter_dir / 'explicacao.qmd'
    title = chapter_dir.name.split(' - ', 1)[1]
    if title in chapters:
        qmd_path.write_text(build_text(title, qmd_path), encoding='utf-8')

print('Atualizados todos os explicacao.qmd com conteúdo detalhado no estilo do seu exemplo.')
