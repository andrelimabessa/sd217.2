import sys

from src.Monolitico.campo_minado_negocio import CampoMinado
from src.Monolitico.campo_minado_negocio import GAME_OVER

# objeto = CampoMinado(4,4)
# objeto.jogada(2,2)
# objeto.imprimir_tabuleiro()

INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"

""" 
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitória

    4. Salvar jogadas
 """


def menu_inicial():
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")


def iniciar_novo_jogo(contexto):
    campo_minado = contexto.get(INSTANCIA)
    campo_minado.criar_novo_jogo(4, 4)
    campo_minado.imprimir_tabuleiro()

    return efetuar_nova_jogada(contexto)


def efetuar_nova_jogada(contexto):
    campo_minado = contexto.get(INSTANCIA)

    while campo_minado.jogadas_restantes > 0:
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        if campo_minado.jogada(linha-1, coluna-1) == GAME_OVER:
            return GAME_OVER

        campo_minado.imprimir_tabuleiro()

    return VITORIA


def sair(contexto):
    sys.exit()


if __name__ == "__main__":

    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    campo_minado = CampoMinado()
    contexto = {INSTANCIA: campo_minado}

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))

        func = switcher.get(opcao)
        print(func(contexto))
