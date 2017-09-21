import sys
from campo_minado_negocio import CampoMinado
from campo_minado_negocio import COORDENADAS_INVALIDAS
from campo_minado_negocio import GAME_OVER
from campo_minado_negocio import JOGADA_SEGURA

INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"

""" 
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitória
    
    4. Salvar jogadas
    5. Continuar jogo 
 """

def menu_inicial(objeto):
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    print(" Selecione uma opção")
    print("1. Criar novo jogo")
    if objeto.jogo_incompleto() == True:
        print("2. Continuar jogo anterior")
    print("9. Sair do Jogo")

def iniciar_novo_jogo(contexto):

    objeto = contexto.get(INSTANCIA)
    objeto.criar_novo_jogo(4,4)
    objeto.imprimir_tabuleiro()

    return efetuar_nova_jogada(contexto)

def continuar_jogo(contexto):
    pass

def efetuar_nova_jogada(contexto):

    objeto = contexto.get(INSTANCIA)

    while objeto.jogadas_restantes > 0:
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        if objeto.jogada(linha,coluna) == GAME_OVER:
            return GAME_OVER
        objeto.imprimir_tabuleiro()
    
    return VITORIA

def sair(contexto):
    sys.exit(0)

if __name__ == "__main__":

    switcher = {
        1: iniciar_novo_jogo,
        2: continuar_jogo,
        9: sair,
    }

    objeto = CampoMinado()
    contexto = {INSTANCIA: objeto}
    
    while True:
        menu_inicial(objeto)
        opcao = int(input("Opção escolhida: "))

        func = switcher.get(opcao)
        print(func(contexto))



