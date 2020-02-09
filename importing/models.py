import uuid
from django.db import models


class Planilha(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    demanda = models.CharField(max_length=150)
    categoria = models.CharField(max_length=30)
    data = models.DateField()
    nome_pessoa = models.CharField(max_length=150)
    tel_pessoa = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(max_length=15, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Planilha'
        
    def __str__(self):
        return "Data: %s - Pessoa: %s - Demanda: %s" % (self.data, self.nome_pessoa, self.demanda)
