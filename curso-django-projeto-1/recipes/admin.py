from django.contrib import admin
from .models import Category, Recipe # Importa a classe Category do models
from django.contrib.contenttypes.admin import GenericStackedInline
from tag.models import Tag

# Register your models here.
class CategoryAdmin(admin.ModelAdmin): # Cria uma classe para personalizar a exibição da classe Category no admin
    ... # colocar esse placeholder para não exigir identação na linha abaixo



admin.site.register(Category, CategoryAdmin) # Registra a classe Category no admin, usando a classe CategoryAdmin para personalização
# o primeiro parâmetro é a classe que será registrada, e o segundo é a classe de personalização

class TagInline(GenericStackedInline):
    model = Tag
    fields = ('nome',)
    extra = 1

@admin.register(Recipe) # Decorador para registrar la clase Recipe en el admin
class RecipeAdmin(admin.ModelAdmin): # Crea una clase para personalizar la visualización de la clase Recipe en el admin
    inlines = [
        TagInline
    ]