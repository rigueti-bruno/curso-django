from django.db import models

# Tabela que receberá os registros dos carros:

class Brand(models.Model):
    id = models.AutoField(primary_key=True) # identificador único do registro de cada marca
    name = models.CharField(max_length=200) # nome da marca do carro
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True) # identificador único do registro de cada carro
    model = models.CharField(max_length=200) # modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,related_name='car_brand') # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação do carro
    model_year = models.IntegerField(blank=True, null=True) # ano do modelo do carro
    value = models.FloatField(blank=True, null=True) # valor do carro
    
    def __str__(self):
        return self.model