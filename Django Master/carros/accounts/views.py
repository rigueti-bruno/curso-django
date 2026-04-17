from django.contrib.auth.forms import UserCreationForm # Importa o formulário de criação de usuário do Django
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST) # verifica se o formulário foi submetido via POST e instancia o formulário com os dados enviados
        if user_form.is_valid(): # verifica se o formulário é válido (todos os campos estão preenchidos corretamente)
            user_form.save() # salva o novo usuário no banco de dados
            return redirect('cars_list') # redireciona para a página de listagem de carros após o registro bem-sucedido
    else:
        user_form = UserCreationForm() # instancia o formulário de criação de usuário
    
    return render(request, 'register.html', {'user_form': user_form}) # renderiza a página de registro, passando o formulário como contexto para o template
