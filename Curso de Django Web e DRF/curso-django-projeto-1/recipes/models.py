from django.db import models
from django.contrib.auth.models import User # Importa a classe User do Django

# Concatenar valores dos campos com Django:
from django.db.models.functions import Concat

# Cria do valor do campo em Annotate:
from django.db.models import Value 

# Utilizado para fazer referência a campos de outro model:
from django.db.models import F

# Importa os os modulos para estabelecer a relação generica entre models:
from django.contrib.contenttypes.fields import GenericRelation
from tag.models import Tag


# Models são classes que representam tabelas no banco de dados.
# Create your models here.

# models.Model indica que a classe herda de models.Model, que é a classe base para todos os modelos do Django.
class Category(models.Model): # cria uma classe para receber as categorias das receitas
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name # método que retorna o nome da categoria quando a instância for convertida para string

class RecipeManager(models.Manager):
    def get_published(self):
        return self.filter(
            is_published=True
        ).annotate(
        author_full_name = Concat(
            F('author__first_name'), Value(" "),
            F('author__last_name'), Value(" "),
            Value("("), F('author__username'), Value(")"))
        ).order_by('-id')

class Recipe(models.Model): # cria uma classe para receber as receitas
    objects = RecipeManager() # substitui o gerenciador padrão do Django pelo gerenciador personalizado RecipeManager
    title = models.CharField(max_length=65) # cria o atributo title que receberá o título da receita
    # o tipo models.CharField é equivalente ao VarChar do SQl, e seu atributo max_length define o tamanho máximo do campo
    description = models.CharField(max_length=165) # atributo que receberá a descrição da receita
    slug = models.SlugField() # atributo especial para URLs, tem um tipo de dado específico
    preparation_time = models.IntegerField() # atributo que receberá o tempo de preparo da receita
    # o tipo models.IntegerField é equivalente ao Int do SQL
    preparation_time_unnit = models.CharField(max_length=65) # atributo que receberá a unidade de tempo do preparo da receita
    servings = models.IntegerField() # atributo que receberá o número de porções da receita
    servings_unit = models.CharField(max_length=65) # atributo que receberá a unidade de medida das porções da receita
    preparation_steps = models.TextField() # atributo que receberá o modo de preparo da receita
    # o tipo models.TextField é equivalente ao Text do SQL, usado para textos longos, sem limite de caracteres
    preparation_steps_is_html = models.BooleanField(default=False) # atributo que indicará se o modo de preparo está em HTML ou não
    # o tipo models.BooleanField é equivalente ao Bool do SQL, usado para valores booleanos (True ou False)
    created_at = models.DateTimeField(auto_now_add=True) # atributo que receberá a data de criação da receita
    # o tipo models.DateTimeField é equivalente ao DateTime do SQL, usado para datas e horas
    # o atributo auto_now_add indica que o campo será preenchido automaticamente com a data e hora atuais quando o objeto for criado
    updated_at = models.DateTimeField(auto_now=True) # atributo que receberá a data de atualização da receita
    # o atributo auto_now indica que o campo será atualizado automaticamente com a data e hora atuais quando o objeto for modificado
    is_published = models.BooleanField(default=False) # atributo que indicará se a receita está publicada ou não
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/') # atributo que receberá a imagem de capa da receita
    # o tipo models.ImageField é usado para armazenar imagens, e o atributo upload_to define o caminho onde a imagem será salva
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,default=None) # atributo que cria um relacionamento com a classe Category
    # o tipo models.ForeignKey é usado para criar relacionamentos entre tabelas
    # o atributo on_delete define o que acontece quando a categoria relacionada é deletada (SET_NULL define que o campo será nulo)
    # o atributo null=True indica que o campo pode ser nulo
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # atributo que cria um relacionamento com a classe User do Django
    # Campo que estabelece a relação genérica entre models:
    tags = GenericRelation(Tag, related_query_name='recipes') # esse atributo identifica a relação genérica

    def __str__(self):
        return self.title # método que retorna o título da receita quando a instância for convertida para string