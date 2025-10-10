from django.shortcuts import render # randeriza os arquivos html e css do site

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

# importa a factory
from utils.recipes.factory import make_recipe

def home(request): # view home
    return render(request,'recipes/pages/home.html', context={'recipes':[make_recipe() for _ in range(10)]})
# a tag 'recipes' receberá os dados gerados pela função make_recipe e com ela serão inseridos os dados no template

def recipe(request, id): # view recipe
    return render(request,'recipes/pages/recipe-view.html', context={
        'recipe':make_recipe(), 
        'is_detail_page':True})