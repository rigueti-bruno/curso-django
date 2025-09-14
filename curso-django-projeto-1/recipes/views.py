from django.shortcuts import render # randeriza os arquivos html e css do site

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

def home(request): # view home
    return render(request,'pages/home.html',status=201, context={'name':"Bruno"})