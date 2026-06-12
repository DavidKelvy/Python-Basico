# Capítulo 18 — Aplicativos e páginas (detalhado)

1) Views e templates (Django)

```python
# urls.py
from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index')]
```

2) Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Dica: use ambientes virtuais e `requirements.txt` para replicabilidade.
