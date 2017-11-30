from django.shortcuts import render
from django.utils import timezone
from .forms import JogadaForm
from .models import Jogada
def post_list(request):
	if request.method == "POST":
		form = JogadaForm(request.POST)
		if form.is_valid():
			jogada = form.save(commit=False)
			jogada.autor = request.user
			jogada.created_date = timezone.now()
			jogada.save()
	else:
		form = JogadaForm()
	jogadas = Jogada.objects.all()
	return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})
# Create your views here.
