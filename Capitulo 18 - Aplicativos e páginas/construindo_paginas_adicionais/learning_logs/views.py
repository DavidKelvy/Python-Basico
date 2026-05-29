# Requisitos: pip install django
# Import: from django.shortcuts import render
from django.shortcuts import render

from .models import Topic


def index(request):
    """A página inicial do Registro de aprendizagem."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostrar todos os tópicos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostrar um único tópico e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)