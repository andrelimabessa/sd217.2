from django.shortcuts import render
from .campo_minado_negocio import CampoMinado
from .forms import CampoMinadoForm




# Create your views here.
def post_list(request):
	return render(request, 'post_list.html', {})

def NovoJogo(request):
	jogo = CampoMinadoForm(request.POST)
	return render(request, 'index.html', {'entrada': jogo})

def Partida(request):
	if request.method == 'POST':
		entrada = CampoMinadoForm(request.POST)
		if entrada.is_valid():
			linha = entrada.cleaned_data['linha']
			coluna = entrada.cleaned_data['coluna']
			objeto = CampoMinado(linha,coluna)
			tabuleiro = objeto.retorna_tabuleiro()
			objeto.salvarJogo()
	else:
		entrada = CampoMinadoForm()

	return render(request, 'tabuleiro.html', {'entrada': entrada, 'tabuleiro': tabuleiro})

def Principal(request):
	objeto = CampoMinado(0,0)
	stats = {}
	stats = objeto.statisticas()
	linMax = stats['linMax']
	colMax = stats['colMax']
	totBomb = stats['totBombas']
	jogadas = stats['totJogadas']
	if request.method == 'POST':
		entrada = CampoMinadoForm(request.POST)
		if entrada.is_valid():
			linha = entrada.cleaned_data['linha']
			coluna = entrada.cleaned_data['coluna']
			perdeu = objeto.jogada(linha,coluna)
			objeto.salvarJogo()
			if perdeu == False:
				if((((linMax-1)*(colMax-1))-(jogadas+1))==totBomb):
					mensagem = 'PARABENS VOCE VENCEU!!!!'
					tabuleiro = objeto.retorna_tabuleiro()
					return render(request, 'fimJogo.html', {'tabuleiro': tabuleiro, 'mensagem': mensagem})
			elif(perdeu == 2):
				mensagem = 'Jogo Salvo!!'
				return render(request, 'fimJogo.html', {'mensagem': mensagem})
			else:
				tabuleiro = objeto.retorna_tabuleiro()
				boardbomba = objeto.matriz_bomba(tabuleiro)
				mensagem = 'KABOOOM!!! Fim de jogo!!'
				return render(request, 'fimJogo.html', {'tabuleiro': boardbomba, 'mensagem': mensagem})

	tabuleiro = objeto.retorna_tabuleiro()
	return render(request, 'tabuleiro.html', {'entrada': entrada, 'tabuleiro': tabuleiro})
	