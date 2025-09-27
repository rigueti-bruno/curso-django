from django.shortcuts import render # randeriza os arquivos html e css do site

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

def home(request): # view home
    return render(request,'recipes/pages/home.html', context={'name':"Bruno"})

def recipe(request, id): # view recipe
    return render(request,'recipes/pages/recipe-view.html', context={'name':"Bruno"})