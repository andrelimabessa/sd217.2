from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .logica import CampoMinado
# Create your views here.

def novo(request):
    return render(request, "index.html", {})

def partida(request):
    tamanho = request.POST
    tabuleiro = CampoMinado(tamanho["linha"], tamanho["coluna"])
    jogadas = tabuleiro.get()
    linha_jogada = int(tamanho["linha-jogada"])
    coluna_jogada = int(tamanho["coluna-jogada"])

    if( jogadas[linha_jogada][coluna_jogada] == "bomba" ):
        resultado = "perdeu troucha"
    else:
        resultado = "ganhou bichão"

    tabuleiro = {
        'jogadas': jogadas,
        'resultado': resultado,
        'linha_jogada': linha_jogada,
        'coluna_jogada': coluna_jogada
    }
    return render(request, 'tabuleiro.html', tabuleiro)
