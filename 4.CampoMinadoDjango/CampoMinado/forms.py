from django import forms

class CampoMinadoForm(forms.Form):
	linha = forms.IntegerField(label='Linha')
	coluna = forms.IntegerField(label='Coluna')

