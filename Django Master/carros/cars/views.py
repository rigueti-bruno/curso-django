from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render #importa a função render
from cars.models import Car # importa os dados do modelo Car para serem utilizados na view

# View/Função que será retornada pelo URL
def carros(request):
    cars = Car.objects.filter(brand__name = "Fiat") # obtém os carros da marca Fiat do banco de dados
    # como brand é uma chave estrangeira, é necessário acessar o nome da marca utilizando a sintaxe brand__name
    return render(request, # requisição recebida do usuário
                  'cars.html', # template que será randerizado e exibido para o usuário
                  {'cars': cars}) # dados que serão passados para o template obtidos do banco de dados