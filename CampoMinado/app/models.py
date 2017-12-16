from django.db import models
from django.utils import timezone

class Jogada(models.Model):
	linha = models.CharField(max_length=2)
	coluna = models.CharField(max_length=2)
	created_date = models.DateTimeField(default=timezone.now)

# Create your models here.
