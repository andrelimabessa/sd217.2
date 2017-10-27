from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json
import sys
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS



INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"
# import sys
# from udp_server import server
# # from udp_cliente import client



# print("Você quer executar:")
# print("1 para servidor")
# print("2 para cliente")
# opcao = input("Opção:")

# try:
#     if int(opcao) == 1:
#         print("Servidor ativado:\n")
#         server()
#     elif int(opcao) == 2:
#         print("Cliente ativado:\n")
#         client()
# except : # pega todas possíveis
#     for val in sys.exc_info():
#         print(val)


# objeto = CampoMinado(2, 2)




def menu_inicial():
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")
    # opcao = int(input("Inserir Opção :"))
    # if opcao == 1:
    #     start()
    # elif opcao == 2:
    #     partida()
    # else:
    #     pass

""" FIM MENU"""



def iniciar_novo_jogo(contexto):

    contexto[QUANTIDADE_LINHAS] = input("Informe a quantidade de linhas: ")
    contexto[QUANTIDADE_COLUNAS] = input("Informe a quantidade de colunas: ")

    return str(contexto)

def continuar_jogo(contexto):
    pass

def efetuar_nova_jogada(contexto):
    pass

def sair(contexto):
    sys.exit(0)



#menu()