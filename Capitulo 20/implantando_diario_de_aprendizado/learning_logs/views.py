from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """A página inicial do Registro de aprendizagem."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Mostrar todos os tópicos."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostrar um único tópico e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    # Certifique-se de que o tópico pertence ao usuário atual.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adicione um novo tópico."""
    if request.method != 'POST':
        # Nenhum dado enviado; crie um formulário em branco.
        form = TopicForm()
    else:
        # Dados POST enviados; processar dados.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Exiba um formulário em branco ou inválido.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adicione uma nova entrada para um tópico específico."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado enviado; crie um formulário em branco.
        form = EntryForm()
    else:
        # Dados POST enviados; processar dados.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Exiba um formulário em branco ou inválido.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edite uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Solicitação inicial; pré-preencher o formulário com a entrada atual.
        form = EntryForm(instance=entry)
    else:
        # Dados POST enviados; processar dados.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)