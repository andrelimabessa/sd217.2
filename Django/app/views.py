from django.shortcuts import render
from .campo_minado_negocio import CampoMinado
from .forms import JogadaForm
from .models import Jogada

VITORIA = "Parabéns você venceu"
COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
GAME_OVER = "Game Over"

objeto = CampoMinado()


def novo_jogo(request):
    jogo = JogadaForm(request.POST)
    return render(request, 'iniciar_jogo.html', {'entrada': jogo})


def partida(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            objeto = CampoMinado()
            objeto.criar_novo_jogo(linha, coluna)
            tabuleiro = objeto.retornar_tabuleiro()
            # objeto.salvarJogo()
    else:
        entrada = JogadaForm()

    mensagem = ''
    return render(request, 'tabuleiro.html', {'entrada': entrada, 'tabuleiro': tabuleiro, 'mensagem': mensagem})


def principal(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            mensagem = objeto.jogada(linha - 1, coluna - 1)
            jogadas_restantes = objeto.jogadas_restantes
            # objeto.salvarJogo()
            if mensagem == VITORIA:
                print("VITORIA ?")
                if jogadas_restantes == 0:
                    print("VITORIA!")
                    tabuleiro = objeto.retornar_tabuleiro
                    return render(request, 'fimJogo.html', {'tabuleiro': tabuleiro, 'mensagem': mensagem})
            elif mensagem == COORDENADAS_INVALIDAS:
                print("COORDENADAS_INVALIDAS")
                tabuleiro = objeto.retornar_tabuleiro
                return render(request, 'tabuleiro.html',
                              {'entrada': entrada, 'tabuleiro': tabuleiro, 'mensagem': mensagem})
            elif mensagem == GAME_OVER:
                print("GAME_OVER")
                tabuleiro = objeto.retornar_tabuleiro
                return render(request, 'fimJogo.html', {'tabuleiro': tabuleiro, 'mensagem': mensagem})
            else:
                print("JOGADA")
                tabuleiro = objeto.retornar_tabuleiro
                return render(request, 'tabuleiro.html',
                              {'entrada': entrada, 'tabuleiro': tabuleiro, 'mensagem': mensagem})
