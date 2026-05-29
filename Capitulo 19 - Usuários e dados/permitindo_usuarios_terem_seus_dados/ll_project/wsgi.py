"""
Configuração WSGI para projeto ll_project.

Ele expõe o WSGI que pode ser chamado como uma variável de nível de módulo chamada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

try:
	from django.core.wsgi import get_wsgi_application
except ImportError:
	raise ImportError("Módulo 'django' não encontrado. Instale com: pip install django") from None

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_wsgi_application()
