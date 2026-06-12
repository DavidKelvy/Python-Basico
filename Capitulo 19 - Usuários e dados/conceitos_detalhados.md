# Capítulo 19 — Usuários e dados (detalhado)

1) Models e autenticação (Django)

```python
from django.db import models
class Topic(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```

2) Views protegidas
- Usar `@login_required` para limitar acesso.

Dica: sempre validar entradas em forms para prevenir dados inválidos.
