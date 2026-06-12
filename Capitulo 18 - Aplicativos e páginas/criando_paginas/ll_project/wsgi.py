"""
Configuração WSGI para projeto ll_project.

Ele expõe o WSGI que pode ser chamado como uma variável de nível de módulo chamada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_wsgi_application()
