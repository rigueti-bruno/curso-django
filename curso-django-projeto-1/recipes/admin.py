from django.contrib import admin
from .models import Category, Recipe # Importa a classe Category do models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin): # Cria uma classe para personalizar a exibição da classe Category no admin
    ... # colocar esse placeholder para não exigir identação na linha abaixo



admin.site.register(Category, CategoryAdmin) # Registra a classe Category no admin, usando a classe CategoryAdmin para personalização
# o primeiro parâmetro é a classe que será registrada, e o segundo é a classe de personalização

@admin.register(Recipe) # Decorador para registrar a classe Recipe no admin
class RecipeAdmin(admin.ModelAdmin): # Cria uma classe para personalizar a exibição da classe Recipe no admin
    ...