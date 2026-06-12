from http.server import BaseHTTPRequestHandler, HTTPServer

html = '''<html>
<head><title>Minha página</title></head>
<body>
<h1>Bem-vindo</h1>
<p>Esta página foi gerada por Python.</p>
</body>
</html>'''

class ServidorSimples(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

porta = 8000
print(f'Servidor preparado para rodar em http://localhost:{porta}')
print('Use este servidor para entregar páginas HTML simples.')
print('Não inicie automaticamente para evitar bloqueio de execução no ambiente atual.')
