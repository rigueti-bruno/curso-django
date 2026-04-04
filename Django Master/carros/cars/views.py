from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render #importa a função render
from cars.models import Car # importa os dados do modelo Car para serem utilizados na view

# View/Função que será retornada pelo URL
def carros(request):
    cars = Car.objects.all().order_by('model') # pega todos os registros do banco de dados na tabela Car
    # order_by ordena os registro pelo paramentro informado de A-Z, nesse caso o campo model
    
    search = request.GET.get('search') # busca na requisição se foi informado algum valor no parametro search
    
    if search: # se for identificado um valor no parametro search
        cars = cars.filter(model__icontains=search) # filtra os registros do banco de dados utilizando o valor do parametro search e o campo model da tabela Car
        # o parametro __icontains retorna os registros com o valor solicitado, independente da forma como o valor foi informado
    
    return render(request, # requisição recebida do usuário
                  'cars.html', # template que será randerizado e exibido para o usuário
                  {'cars': cars}) # dados que serão passados para o template obtidos do banco de dados ou do filtro realizado com o parametro search