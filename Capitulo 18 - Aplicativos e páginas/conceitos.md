# Capítulo 18 — Aplicativos e páginas

Este capítulo explica conceitos de Django e desenvolvimento web.

## Projeto Django
- Um projeto Django pode conter configurações e URLs.
- `manage.py` é usado para comandos do framework.

## App
- App é um componente do projeto.
- Contém `views.py`, `models.py`, `urls.py` e `templates`.

## URLs
- Mapear URLs para funções ou classes de view.
- Usam `path()` em `urls.py`.

## Views
- Funções que retornam páginas ou respostas.
- Podem renderizar templates.

## Templates
- HTML com sintaxe Django para mostrar dados.
- Use variáveis e laços no template.

## Migrations
- Migrations atualizam o esquema do banco de dados.
- Criadas com `makemigrations` e aplicadas com `migrate`.
