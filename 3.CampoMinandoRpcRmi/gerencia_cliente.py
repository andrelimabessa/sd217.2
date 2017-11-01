import sys
from jsonrpclib import Server

INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"
GAME_OVER = "Game Over"
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


def iniciar_novo_jogo(proxy):

    linha = int(input("Informe a quantidade de linhas: "))
    coluna =int(input("Informe a quantidade de colunas: "))
    proxy.criar_novo_jogo(linha, coluna)
    # tabuleiro = proxy.retorna_tabuleiro()
    #
    # for posicao in tabuleiro:
    #     print(str(posicao))

    imprimir_tabuleiro(proxy.retorna_tabuleiro())

    return efetuar_nova_jogada(proxy)


def efetuar_nova_jogada(proxy):
    # while 10 > 0:
    while proxy.jogadas_restantes() > 0:
        print(proxy.jogadas_restantes)
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        proxy.efetuar_jogada(linha,coluna)
        # if proxy.efetuar_jogada(linha-1, coluna-1) == GAME_OVER:
        #     return GAME_OVER

        imprimir_tabuleiro(proxy.retorna_tabuleiro())

    return VITORIA


def sair(proxy):
    sys.exit()


def imprimir_tabuleiro(tabuleiro):
    for posicao in tabuleiro:
        print(str(posicao))


def client():
    proxy = Server('http://localhost:7002')
    # print(proxy.print_name("André", "Bessa"))
    # print(proxy.criar_novo_jogo(4,4))
    # proxy.criar_novo_jogo(4,4)
    # imprimir_tabuleiro(proxy.retorna_tabuleiro())


    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))
        func = switcher.get(opcao)
        print(func(proxy))
