from django import forms # importa a biblioteca de formulários do Django para criar formulários personalizados
from cars.models import Brand # importa os dados do modelo Brand para serem utilizados no formulário como chave estrangeira

class CarForm(forms.Form): # define uma classe com os Campos do Formulário a ser exibido para o usuário
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # recebe os dados do Model Brand para serem selecionados
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

# Como o formulário preencherá os campos do Model Car, ele deve ter todos os campos do modelo.