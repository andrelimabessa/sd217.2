from django import forms
from .models import Jogada


class JogadaForm(forms.Form):

    linha = forms.IntegerField(label='Linha')
    coluna = forms.IntegerField(label='Coluna')


    # class Meta:
    #     model = Jogada
    #     fields = ('linha', 'coluna')
