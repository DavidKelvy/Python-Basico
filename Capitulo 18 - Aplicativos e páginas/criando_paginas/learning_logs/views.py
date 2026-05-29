# Requisitos: pip install django
# Import: from django.shortcuts import render
from django.shortcuts import render


def index(request):
    """A página inicial do Registro de aprendizagem."""
    return render(request, 'learning_logs/index.html')
