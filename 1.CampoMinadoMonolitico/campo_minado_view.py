from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json

objeto = CampoMinado(10, 10)
objeto.imprimir_tabuleiro()

def iniciar_jogo():
    if objeto.proxima_jogada():
        linha = int(input("Qual linha você deseja ir? "))
        coluna = int(input("Qual coluna você deseja ir? "))
        objeto.jogada(linha,coluna)
        iniciar_jogo()
    else:
        print("Fim! Joga novamente!!!")

def iniciar_partida():
    if isfile("game.json"):
        result = str(input("Quer continuar um jogo salvo? \n"))
        if result == "yes":
            arquivo = open("game.json")
            game = json.loads(arquivo.read())

            objeto.restaurar(game)
            arquivo.close()
        else:
            remove("game.json")

    iniciar_partida()

partida()
