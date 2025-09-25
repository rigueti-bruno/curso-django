from django.urls import path
from . import views # importação das views do app recipes

urlpatterns = [
    path('', views.home), # Inclui o conteudo da view home na pagina inicial/raiz do site
    path('recipe/<int:id>/', views.recipe), # Inclui o conteudo da view recipe na pagina recipe/i
    ]