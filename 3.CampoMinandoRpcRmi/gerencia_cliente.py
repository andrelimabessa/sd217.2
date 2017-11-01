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
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")

def total_jogadas(proxy):
    qtd = proxy.total()
    print(qtd)




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

    while proxy.continuar():
        #print(proxy.continuar())
        qtd = proxy.jogadas_restantes()
        print("JOGADAS RESTESTANTES : ",qtd)
        linha = int(input("[Jogada]  Informe a  linha: "))
        coluna = int(input("[Jogada] Informe a coluna: "))
        if proxy.efetuar_jogada(linha, coluna) == GAME_OVER:
            return GAME_OVER
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
        3: sair,
    }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))
        func = switcher.get(opcao)
        print(func(proxy))
