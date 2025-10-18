from django.shortcuts import render # randeriza os arquivos html e css do site

from django.shortcuts import get_list_or_404 # importa o atalho para retornar 404 se a lista estiver vazia

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

# importa a factory
from utils.recipes.factory import make_recipe

# importa o model Recipe
from .models import Recipe

# Importa as respostas de erro HTTP
from django.http import HttpResponse, Http404

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
    recipes = get_list_or_404(Recipe.objects.filter( # o get_list_or_404 retorna 404 se a lista estiver vazia
        category__id=category_id,
        is_published=True,
        ).order_by('-id')) # obtem os dados da tabela Recipe e ordena por id decrescente
    
    return render(request,'recipes/pages/category.html', context={
        'recipes': recipes, #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
        'title': f'{recipes[0].category.name} - Category', #pega o nome da categoria do primeiro item da lista
})