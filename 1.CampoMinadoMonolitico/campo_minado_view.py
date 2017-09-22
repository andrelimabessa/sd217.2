from campo_minado_negocio import CampoMinado
import os
import sys
"""
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra para vitoria

    4. Salvar jogadas
    5. Continuar jogo

"""

""" Variavel Local de Impressao do Tabuleiro """
board = []

""" Variavel Local de Impressao do Tabuleiro de Bombas """
boardbomba = []

""" Funcao para imprimir o Tabuleiro """
def imprimir_tabuleiro(board):
        for posicao in board:
            print(str(posicao))

""" Funcao Principal do Jogo """
def principal(objeto,linMax,colMax):
    """ Total de Jogadas """
    jogadas = 0

    """ Variavel de Controle do Loop """
    perdeu = False

    """ Variavel com o total de Bombas """
    qtd_bombas = objeto.total_bombas()

    """ Sem uso no momento """    
    msg = 0

    """ Loop principal do Jogo """
    while not(perdeu):
        unused_variable = os.system("clear")
        print("Digite 0 na linha e 0 na coluna para Salvar e Sair")
        board = objeto.retorna_tabuleiro()
        imprimir_tabuleiro(board)
        lin = int(input("Digite a linha: "))
        col = int(input("Digite a coluna: "))
        perdeu = objeto.jogada(lin,col,msg)
        jogadas = jogadas + 1
        """ Testando se o jogador Venceu,
            se o jogo foi salvo ou se o jogador
            perdeu. """
        if(perdeu == False):
            if (((linMax)*(colMax))-jogadas) == int(qtd_bombas):
                print("\nPARABENS!! VOCE VENCEU!!!")
                perdeu = True
        elif(perdeu == 2):
            print("Jogo Salvo!!!\n")
            sys.exit(0)
        else:
            boardbomba = objeto.matriz_bomba(board)
            imprimir_tabuleiro(boardbomba)
            print("KABOOOM!!! Fim de jogo!!")
            
    """ Teste para continuar ou sair. """
    flag = str(input("Jogar de novo S/N?"))
    if(flag == 's' or flag == 'S'):
        """ Se Quiser continuar Verdadeiro """
        board = []
        return True
    else:
        """ Caso contrario Falso """
        return False


""" Funcao para Iniciar um Jogo Novo """
def novoJogo():
    jogar = True
    while(jogar):
        unused_variable = os.system("clear")
        linMax = int(input("Digite o total de linhas: "))
        colMax = int(input("Digite o total de colunas: "))
        objeto = CampoMinado(linMax,colMax)
        jogar = principal(objeto,linMax,colMax)

""" * Funcao para carregar um jogo Salvo *
    Cria um novo objeto, chama o metodo carregarJogo no servidor 
    para carregar a partida anterior e devolve o total de linhas
    e colunas para calculo da derrota. Em seguida continua a partida
    e em caso de derrota entra no loop de um jogo novo. """
def carregar_Jogo():
    objeto = CampoMinado(0,0)
    opt = objeto.carregarJogo()
    linha = opt['linha']
    coluna = opt['coluna']
    linMax = linha-1
    colMax = coluna-1
    jogar = principal(objeto,linMax,colMax)
    novoJogo()

""" ** Funcao do MENU do jogo **
    Cria uma lista com as opcoes, aguarda o jogador
    escolher uma delas em seguida chama a funcao
    escolhida. """
def Menu():
    listaMenu = ['Novo Jogo', 'Continuar','Sair']

    unused_variable = os.system("clear")
    print(" CAMPO MINADO ","\n\n")
    print(" MENU ","\n")
    for i, v in enumerate(listaMenu):
        print(i+1, v,"\n\n")

    opcao = input("Escolha uma opcao: ")
    if(opcao == '1'):
        novoJogo()
    elif(opcao == '2'):
        carregar_Jogo()
    else:
        sys.exit(0)

""" Inicia o jogo chamando a funcao do Menu e 
    a partir dela resolve as demais pendencias."""
Menu()