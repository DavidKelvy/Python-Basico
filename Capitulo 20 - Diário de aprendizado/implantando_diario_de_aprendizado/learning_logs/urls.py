"""Define padrões de URL para learning_logs."""

try:
    from django.urls import path
except ImportError:
    raise ImportError("Módulo 'django' não encontrado. Instale com: pip install django") from None

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # Página que mostra todos os tópicos.
    path('topics/', views.topics, name='topics'),
    # Página de detalhes para um único tópico.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Página para adicionar um novo tópico.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Página para adicionar uma nova entrada.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Página para editar uma entrada.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]