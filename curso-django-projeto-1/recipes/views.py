from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

def home(request): # view home
    return render(request,'recipes/home.html',status=201, context={'name':"Bruno"})

def sobre(request):
    return HttpResponse('SOBRE 3') # função que retorna uma "Response" genérica indicada pela função HTTPResponse

def contato(request):
    return HttpResponse('CONTATO 3')