"""
Configuração ASGI para o projeto ll_project.

Ele expõe o ASGI que pode ser chamado como uma variável de nível de módulo chamada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_asgi_application()
