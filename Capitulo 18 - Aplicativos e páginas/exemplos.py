# Exemplo 1: Gerar HTML
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
