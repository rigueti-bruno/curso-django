from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importa os formulários de criação de usuário e login do Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST) # verifica se o formulário foi submetido via POST e instancia o formulário com os dados enviados
        if user_form.is_valid(): # verifica se o formulário é válido (todos os campos estão preenchidos corretamente)
            user_form.save() # salva o novo usuário no banco de dados
            return redirect('login') # redireciona para a página de listagem de carros após o registro bem-sucedido
    else:
        user_form = UserCreationForm() # instancia o formulário de criação de usuário
    
    return render(request, 'register.html', {'user_form': user_form}) # renderiza a página de registro, passando o formulário como contexto para o template

def login_view(request):
    if request.method == "POST": # verifica se o método da requisão é POST
        username = request.POST["username"] # verifica o usuário informado
        password = request.POST["password"] # verifica a senha informada
        
        user = authenticate(request, username=username, password=password)
        # captura os valores informados no formulário
        # verifica se há um usuário que tenha o nome e a senha informados e o captura
        
        if user is not None: # se o o usuário for localizado com os dados informados
            login(request, user) # executa o login
            
            return redirect('cars_list') # redireciona para a lista de carros
        else: # se o usuário não for localizado
            login_form = AuthenticationForm() # redireciona novamente para tela de login em branco
    else:        
        login_form = AuthenticationForm() # vincula um formulario de login limpo se for o primeiro acesso à página
    return render(request, 'login.html', {'login_form': login_form}) # randeriza o template de login

def logout_view(request):
    logout(request) # executa o logout do usuário
    return redirect('cars_list') # redireciona para a lista de carros após o logout