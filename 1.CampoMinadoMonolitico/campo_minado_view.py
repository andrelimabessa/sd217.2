from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json

objeto = CampoMinado(2, 2)
objeto.imprimir_tabuleiro()

print("-------------------- Campo Minado -----------------------")
print("---------------------------------------------------------")



def start ():
    if objeto.proxima_jogada():
        linha = int(input("Posição da linha :"))
        coluna = int(input("Posição da coluna :"))
        objeto.jogada(linha,coluna)
        start()
    else:
        print("Fim")


def partida():
    if isfile("game.json"):
        result = str(input("Quer continuar um jogo salvo?\n"))
        if result == "yes":
            arquivo = open("game.json")
            game = json.loads(arquivo.read())

            objeto.restaurar(game)
            arquivo.close()
        else:
            remove("game.json")

    start()

partida()