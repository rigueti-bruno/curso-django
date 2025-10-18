from django.shortcuts import render # randeriza os arquivos html e css do site

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

# importa a factory
from utils.recipes.factory import make_recipe

# importa o model Recipe
from .models import Recipe

def home(request): # view home
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id') # obtem os dados da tabela Recipe e ordena por id decrescente
    return render(request,'recipes/pages/home.html', context={
        'recipes': recipes #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
        })
    
def recipe(request, id): # view recipe
    recipes = Recipe.objects.all().order_by('-id') # obtem os dados da tabela Recipe e ordena por id decrescente
    return render(request,'recipes/pages/recipe-view.html', context={
        'recipes': recipes #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
})

def category(request,category_id): # view category
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id') # obtem os dados da tabela Recipe e ordena por id decrescente
    return render(request,'recipes/pages/category.html', context={
        'recipes': recipes #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
})