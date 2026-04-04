from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render #importa a função render
from cars.models import Car # importa os dados do modelo Car para serem utilizados na view
from cars.forms import CarForm # importa os dados do formulário CarForm para serem utilizados na view

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
    
def new_car_view(request):
    new_car_form = CarForm() # cria um formulário vazio utilizando a classe CarForm
    
    return render(
        request,
        'new_car.html', # vincula o template do formulário à view
        {'new_car_form': new_car_form} # vincula o formulário criado à view para ser utilizado no template
    )