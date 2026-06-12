# Capítulo 20 — Diário de aprendizado

Este capítulo trata de preparar um projeto para uso real.

## requirements.txt
- Lista dependências do projeto.
- Instale com `pip install -r requirements.txt`.

## Configurações de produção
- `DEBUG = False` para modo produção.
- `ALLOWED_HOSTS` define domínios permitidos.

## Variáveis de ambiente
- Armazene segredos fora do código.
- Use `os.environ.get()` para ler valores.

## Páginas de erro
- Crie páginas como `404.html` e `500.html`.
- Melhor experiência de usuário em erros.

## Arquivos estáticos
- Organize CSS, JavaScript e imagens.
- Configure coleta de arquivos estáticos em projetos web.
