"""Capítulo 18: Aplicativos e páginas
Este arquivo mostra uma estrutura simples de aplicativo com páginas.
"""

paginas = ['home', 'sobre', 'contato']
for pagina in paginas:
    print('Página disponível:', pagina)

pagina_atual = 'home'
if pagina_atual == 'home':
    print('Exibindo a página inicial')
