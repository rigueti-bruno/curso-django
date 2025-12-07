from django.urls import path

from . import views # importação das views do app recipes

app_name = 'recipes' # namespace do app recipes

urlpatterns = [
    path('', views.home,name='home'), # Inclui o conteudo da view home na pagina inicial/raiz do site
    path('recipes/category/<int:category_id>/',views.category,name='category'), # Inclui o conteudo da view category na pagina recipes/category/int:category_id/
    path('recipes/<int:id>/', views.recipe,name='recipe'), # Inclui o conteudo da view recipe na pagina recipe/i
    path(
        'recipes/theory/',
         views.theory,
         name='theory'), # Inclui o conteudo da view theory na pagina recipe/theory/
    ]