"""Define padrões de URL para contas."""

from django.urls import path, include

from . import views


app_name = 'accounts'
urlpatterns = [
    # Inclui URLs de autenticação padrão.
    path('', include('django.contrib.auth.urls')),
    # Página de registro.
    path('register/', views.register, name='register'),
]