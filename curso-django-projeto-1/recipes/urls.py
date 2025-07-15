from django.urls import path
from recipes.views import home, sobre, contato

urlpatterns = [
    path('',home), # Inclui o conteudo da view home na pagina inicial/raiz do site
    path('sobre/',sobre), # inclui o conteudo da view sobre na pagina sobre
    path('contato/',contato) # inclui o conteudo da view contato na pagina contato
]