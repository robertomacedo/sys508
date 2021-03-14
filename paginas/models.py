from django.db import models


class Pessoa(models.Model):
    name = models.CharField(max_length=50, blank=False)
    nascimento = models.DateField(blank=True, null=True)
    contato = models.CharField(max_length=15)
    mae = models.CharField(max_length=50, blank=False)
    pai = models.CharField(max_length=50, blank=True, null=True)
    datecadastro = models.DateTimeField(auto_now_add=True)
    dateupgrade = models.DateTimeField(auto_now=True)


