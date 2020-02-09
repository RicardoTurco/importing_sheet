import uuid
from django.db import models


class Planilha(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    demanda = models.CharField(max_length=150)
    categoria = models.CharField(max_length=30)
    data = models.DateField()
    nome_pessoa = models.CharField(max_length=150)
    tel_pessoa = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(15, null=True, blank=True)
