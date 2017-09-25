from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json

objeto = CampoMinado(2, 2)




def menu():
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")
    opcao = int(input("Inserir Opção :"))
    if opcao == 1:
        start()
    elif opcao == 2:
        partida()
    else:
        pass

""" FIM MENU"""

def start ():
    if objeto.proxima_jogada():
        objeto.imprimir_tabuleiro()
        linha = int(input("Posição da linha :"))
        coluna = int(input("Posição da coluna :"))
        objeto.jogada(linha,coluna)
        start()
    else:
        print("Fim")


def partida():
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        objeto.restaurar(game)
        arquivo.close()
        start()
    else:
        print("Não há jogo salvo !\n")
        




menu()
