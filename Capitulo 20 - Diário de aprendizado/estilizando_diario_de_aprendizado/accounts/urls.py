"""Define padrões de URL para contas."""

# Requisitos: pip install django
# Import: from django.urls import path, include
from django.urls import path, include

from . import views


app_name = 'accounts'
urlpatterns = [
    # Inclui URLs de autenticação padrão.
    path('', include('django.contrib.auth.urls')),
    # Página de registro.
    path('register/', views.register, name='register'),
]