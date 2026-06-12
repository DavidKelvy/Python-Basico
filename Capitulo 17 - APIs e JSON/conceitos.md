# Capítulo 17 — APIs e JSON

Conceitos principais:

- **APIs web**: obter dados via HTTP (GET requests) de serviços externos.
- **módulo `requests`**: enviar requisições e receber respostas (status codes, headers, conteúdo).
- **JSON**: `response.json()` ou `json.loads()` para converter texto em estruturas Python (dict/list).
- **paginação e limites**: lidar com múltiplas páginas de resultados e limites de taxa (rate limiting).
- **tratamento de erros de rede**: checar `status_code`, usar `try/except` e timeout.
- **visualização de dados de API**: extrair campos relevantes e representar em gráficos.

APIs e JSON conectam o programa a serviços e dados externos.
