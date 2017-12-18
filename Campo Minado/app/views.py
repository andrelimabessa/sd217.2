from django.shortcuts import render
from .models import Jogada
from .forms import JogadaForm
from .campoMinado import CampoMinado

obj = CampoMinado()

def novoJogo(request): 
    return render(request, 'novoJogo.html', {'jogadaForm': JogadaForm(request.POST)})

def partida(request):
    global obj
    if request.method == 'POST':
        jogadaForm = JogadaForm(request.POST)
        if jogadaForm.is_valid():
            linha = jogadaForm.cleaned_data['linha']
            coluna = jogadaForm.cleaned_data['coluna']
            obj = CampoMinado()
            obj.criarNovoJogo(linha, coluna)
            campo = obj.retornarCampo()
    else:
        jogadaForm = JogadaForm()

    msg = ''
    return render(request, 'campo.html', {'jogadaForm': jogadaForm, 'campo': campo, 'msg': msg})

def principal(request):
    global obj
    if request.method == 'POST':
        jogadaForm = JogadaForm(request.POST)
        if jogadaForm.is_valid():
            linha = jogadaForm.cleaned_data['linha']
            coluna = jogadaForm.cleaned_data['coluna']
            msg = obj.jogada(linha - 1, coluna - 1)
            proxJogadas = obj.proxJogadas 

            if msg == "Jogada Inválida!!":
                campo = obj.retornarCampo
                print("Jogada Inválida!!")
                return render(request, 'campo.html',
                {'jogadaForm': jogadaForm, 'campo': campo, 'msg': msg})
            elif msg == "Fim de Jogo!!":
                campo = obj.retornarCampo
                print("Fim de Jogo!!")
                return render(request, 'fimJogo.html', {'campo': campo, 'msg': msg})
            elif msg == "Você Ganhou!!":
                if proxJogadas == 0:
                    campo = obj.retornarCampo
                    print("Você Ganhou!!")
                    return render(request, 'fimJogo.html', {'campo': campo, 'msg': msg})        
            else:
                campo = obj.retornarCampo
                return render(request, 'campo.html',
                              {'jogadaForm': jogadaForm, 'campo': campo, 'msg': msg})
