from django.shortcuts import render


def index(request):
    """A página inicial do Registro de aprendizagem."""
    return render(request, 'learning_logs/index.html')
