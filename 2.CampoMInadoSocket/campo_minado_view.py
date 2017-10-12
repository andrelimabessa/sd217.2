import sys
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS

INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"

def menu_inicial():
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")

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
