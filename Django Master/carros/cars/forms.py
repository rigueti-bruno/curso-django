from django import forms # importa a biblioteca de formulários do Django para criar formulários personalizados
from cars.models import Brand, Car # importa os dados do modelo Brand para serem utilizados no formulário como chave estrangeira
# Importa o model Car para salvar os dados do formulário no banco de dados utilizando o método save() do formulário

class CarForm(forms.Form): # define uma classe com os Campos do Formulário a ser exibido para o usuário
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # recebe os dados do Model Brand para serem selecionados
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

# Como o formulário preencherá os campos do Model Car, ele deve ter todos os campos do modelo.
    def save(self): # método para salvar os dados do formulário no banco de dados
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
        )
        car.save() # salva os dados do formulário no banco de dados utilizando o método save() do model Car
        return car