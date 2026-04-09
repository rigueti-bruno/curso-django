from django import forms # importa a biblioteca de formulários do Django para criar formulários personalizados
from cars.models import Brand, Car # importa os dados do modelo Brand para serem utilizados no formulário como chave estrangeira
# Importa o model Car para salvar os dados do formulário no banco de dados utilizando o método save() do formulário

"""
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
"""
# O código acima é um exemplo de como criar um formulário utilizando a classe forms.Form do Django

    
class CarModelForm(forms.ModelForm):
    class Meta: # define a classe Meta para configurar o formulário baseado no modelo Car
        model = Car # define que o formulário é baseado no modelo Car
        fields = '__all__' # define que todos os campos do modelo Car serão utilizados no formulário
        
    # Vamos inserir abaixo as regras de validação para os campos do formulário utilizando o método clean() do formulário

    # Exigindo que o carro tenha o valor acima de R$20.000:
    def clean_value(self):
        value = self.cleaned_data.get('value') # captura o campo com o valor informado para o carro
        
        if value < 20000:
            self.add_error('value', 'O valor mínimo deve ser R$20.000,00') # define a regra de validação para o campo
        
        return value # caso o valor seja valido, ele é retornado para seguir o cadastro.
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year') # captura o ano de fabricação do carro
        
        if factory_year < 1975:
            self.add_error('factory_year', 'O carro deve ser mais novo!') # define a regra de validação
            
        return factory_year # permite seguir o cadastro caso o ano seja válido