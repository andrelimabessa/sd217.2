from django import forms

class JogadaForm(forms.Form):
	linha = forms.IntegerField(label='Linha')
	coluna = forms.IntegerField(label='Coluna')