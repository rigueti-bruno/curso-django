from django.shortcuts import render # randeriza os arquivos html e css do site

from django.shortcuts import get_list_or_404 # importa o atalho para retornar 404 se a lista estiver vazia

from django.shortcuts import get_object_or_404 # importa o atalho para retornar 404 se o objeto nao for encontrado

# Create your views here.
from django.http import HttpResponse # dependencia da view - cria a response

# importa a factory
from utils.recipes.factory import make_recipe

# importa o model Recipe
from .models import Recipe

# Importa as respostas de erro HTTP
from django.http import HttpResponse, Http404

# Importa o erro de valor inexistente:
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q

# Utilizado para fazer referência a campos de outro model:
from django.db.models import F

# Importar funções de agregação:
from django.db.models.aggregates import Count, Avg, Sum, Min, Max

# Cria do valor do campo em Annotate:
from django.db.models import Value 

# Concatenar valores dos campos com Django:
from django.db.models.functions import Concat

def home(request): # view home
    recipes = get_list_or_404(Recipe,is_published=True)# obtem os dados da tabela Recipe e ordena por id decrescente
    return render(request,'recipes/pages/home.html', context={
        'recipes': recipes #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
        })
    
def recipe(request, id): # view recipe
    recipe = get_object_or_404(Recipe, pk=id,is_published=True) # obtem os dados da tabela Recipe pelo id ou retorna 404 se nao encontrar
    
    return render(request,'recipes/pages/recipe-view.html', context={
        'recipe': recipe, #substituimos os dados gerados aleatoriamente pela consulta ao banco de dados
        'is_detail_page': True,
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

def theory(request,*args,**kwargs):
    recipes = Recipe.objects.get_published() # executa todas as consultas do gerenciador personalizado RecipeManager
    
    number_of_recipes = recipes.aggregate(Count('id'))
    context = {
        'recipes':recipes,
        'number_of_recipes':number_of_recipes['id__count'],
        } # contexto da view, 'recipes':recipes recebe os dados do queryset
    return render(
        request,
        'recipes/pages/theory.html',
        context=context
    )