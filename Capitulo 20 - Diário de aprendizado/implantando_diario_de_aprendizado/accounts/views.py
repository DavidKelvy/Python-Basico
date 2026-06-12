from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registre um novo usuário."""
    if request.method != 'POST':
        # Exiba o formulário de registro em branco.
        form = UserCreationForm()
    else:
        # Processar formulário preenchido.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faça login do usuário e redirecione para a página inicial.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Exiba um formulário em branco ou inválido.
    context = {'form': form}
    return render(request, 'registration/register.html', context)