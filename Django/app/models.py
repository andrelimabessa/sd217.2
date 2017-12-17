from django.db import models
from django.utils import timezone


class Jogada(models.Model):
    linha = models.IntegerField()
    coluna = models.IntegerField()
