from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render #importa a função render

# View/Função que será retornada pelo URL
def carros(request):
    return render(request, # requisição recebida do usuário
                  'cars.html', # template que será randerizado e exibido para o usuário
                  {'cars':{'model1':'Astra 2.0','model2':'Mustang GT'}}) # dados que serão passados para o template