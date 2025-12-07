import string
from random import SystemRandom
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    # Aqui começa os campos para a relação genérica:
    
    # Indica o model ao qual a tag será associada:
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    
    # Representa o id da linha do model associado:
    object_id = models.CharField(max_length=255)
    
    # Representa a relação genéruca que une os dois campos acima:
    content_object = GenericForeignKey('content_type', 'object_id')
    
    # Metodo que configura o slug antes de salvar:
    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = "".join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits, # indica os tipos de caracteres do slug
                    k=5 # indica a quantidade de caracteres do slug (5 nesse caso)
                )
            )
            self.slug = slugify(f"{self.nome}-{rand_letters}")
        return super().save(*args, **kwargs)
    
    # Defune a representação em string do objeto:
    def __str__(self):
        return self.nome