from django.urls import path

from . import views # importação das views do app recipes

app_name = 'recipes' # namespace do app recipes

urlpatterns = [
    path('', views.home,name='home'), # Inclui o conteudo da view home na pagina inicial/raiz do site
    path('recipe/<int:id>/', views.recipe,name='recipe'), # Inclui o conteudo da view recipe na pagina recipe/i
    ]