from django.urls import path
from recipes.views import home

urlpatterns = [
    path('',home), # Inclui o conteudo da view home na pagina inicial/raiz do site
    ]