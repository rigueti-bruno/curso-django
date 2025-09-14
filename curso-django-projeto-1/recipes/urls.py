from django.urls import path
from recipes.views import home # importação das views do app recipes

urlpatterns = [
    path('',home), # Inclui o conteudo da view home na pagina inicial/raiz do site
    ]