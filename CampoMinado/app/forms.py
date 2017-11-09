from django import forms
from .models import Jogada

class JogadaForm(forms.ModelForm):            
	class Meta:
		model = Jogada
		fields = ('linha','coluna')