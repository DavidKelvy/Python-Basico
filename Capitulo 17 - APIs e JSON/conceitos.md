# Capítulo 17 — APIs e JSON

Este capítulo mostra como buscar dados da web.

## API
- API é uma interface para acessar dados ou serviços.
- Normalmente usa HTTP.

## requests
- `requests.get(url)` envia requisição à API.
- `response.status_code` verifica se deu certo.

## JSON
- JSON é um formato de dados em texto.
- `response.json()` converte JSON em dicionários e listas.

## Tratamento de erros
- `try/except` captura falhas de conexão ou resposta inválida.
- Verifique `status_code` antes de usar os dados.
