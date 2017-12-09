from django import forms
from .models import *

class JogadaForm(forms.ModelForm):
    class Meta:
        model = Jogada
        fields = ('linha','coluna')


class CriaTabuleiro(forms.ModelForm):
    class Meta:
        model = Tabuleiro
        fields = ('linhas', 'colunas')