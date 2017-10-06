import socket
import os
import sys
from ast import literal_eval
import platform

""" ******************************
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra para vitoria

    4. Salvar jogadas
    5. Continuar jogo
******************************* """

""" Variavel Local de Impressao do Tabuleiro """
board = []

""" Variavel Local de Impressao do Tabuleiro de Bombas """
boardbomba = []

""" Funcao para limpar a tela do prompt """
def limpaTela():
    so = platform.system()
    if(so != 'Windows'):
        unused_variable = os.system("clear")
    else:
        unused_variable = os.system("cls")

""" Funcao para imprimir o Tabuleiro """
def imprimir_tabuleiro(board):
        for posicao in board:
            print(str(posicao))

""" Funcao Principal do Jogo """
def principal(conexao,linMax,colMax):
    """ ****************************************************************
        Criando dicionario com informacoes para envio ao servidor
        - Envio, recebimento e tratamento das informacoes
        - Esse processo se repete em diversas outras partes do codigo.
    **************************************************************** """
    objetoConS = {'tipo':'novoJogo', 'linMax': linMax,'colMax':colMax}
    conexao.sendall(str(objetoConS).encode())
    objetoConR  = conexao.recv(1024).decode()
    objeto = literal_eval(objetoConR)
        
    """ Total de Jogadas """
    jogadas = 0

    """ Variavel de Controle do Loop """
    perdeu = False

    """ Variavel com o total de Bombas """
    qtd_bombas = objeto['totalBombas']

    """ Se estiver continuando jogo carrega total de linhas e colunas """
    if(linMax == 0 and colMax == 0):
        linMax = objeto['linha']
        colMax = objeto['coluna']

    """ Sem uso no momento """    
    msg = 0

    """ Loop principal do Jogo """
    while not(perdeu):
        limpaTela()
        print("Digite 0 na linha e 0 na coluna para Salvar e Sair")
        """ Imprimindo Tabuleiro """
        objetoConS = {'tipo':'retorna_tabuleiro'}
        conexao.sendall(str(objetoConS).encode())
        objetoConR  = conexao.recv(1024).decode()
        board = literal_eval(objetoConR)
        imprimir_tabuleiro(board)
        """ *** """
        lin = int(input("Digite a linha: "))
        col = int(input("Digite a coluna: "))
        """ Enviando jogada para o servidor e precessando resposta """
        objetoConS = {'tipo':'jogada','linha':lin,'coluna':col}
        conexao.sendall(str(objetoConS).encode())
        objetoConR  = conexao.recv(1024).decode()
        perdeu = literal_eval(objetoConR)
        jogadas = jogadas + 1
        """ ***************************************
            Testando se o jogador Venceu,
            se o jogo foi salvo ou se o jogador
            perdeu.
        *************************************** """
        if(perdeu == False):
            if (((linMax)*(colMax))-jogadas) == int(qtd_bombas):
                print("\nPARABENS!! VOCE VENCEU!!!")
                perdeu = True
        elif(perdeu == 2):
            print("Jogo Salvo!!!\n")
            sys.exit(0)
        else:
            """ Imprimindo a matriz resultado da derrota """
            objetoConS = {'tipo':'matriz_bomba','board':board}
            conexao.sendall(str(objetoConS).encode())
            objetoConR  = conexao.recv(1024).decode()
            boardbomba = literal_eval(objetoConR)
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
def novoJogo(conexao):
    jogar = True

    """ ****************************************************************
        Loop da funcao de novoJogo continua iniciando um jogo novo ate
        o jogador decidir sair no momento da derrota.
    **************************************************************** """  
    while(jogar):
        limpaTela()
        linMax = int(input("Digite o total de linhas: "))
        colMax = int(input("Digite o total de colunas: "))
        jogar = principal(conexao,linMax,colMax)
    """ Fechando a conexao com o servidor """
    conexao.close()

""" *************************************************************************
    FUNCAO PARA CARREGAR UM JOGO SALVEO:
    Chama a funcao 'principal' passando como parametros a conexao
    e o total de linhas e colunas como Zero o que simboliza carregar
    um jogo novo no servidor. Apos finalizada a partida que foi carregada
    chama uma nova partida e comeca jogo novo se o jogador nao tiver optado
    por sair.
************************************************************************** """
def carregar_Jogo(conexao):
    principal(conexao,0,0)
    novoJogo(conexao)
    conexao.close()

""" *************************************************************************** 
    FUNCAO DO MENU DO JOGO:
    - Inicia a conexao do jogo com o servidor e repassa essa conexao as demais
    funcoes que serao selecionadas;
    - Cria uma lista com as opcoes, aguarda o jogador
    escolher uma delas em seguida chama a funcao
    escolhida.
*************************************************************************** """
def Menu():

    """ Endereco do Servidor e a Porta """
    HOST = '127.0.0.1'
    PORT = 9999
    """ Iniciando a conexao com o servidor e armazenando a mesma na variavel 'conexao' """
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.connect((HOST, PORT))

    listaMenu = ['Novo Jogo', 'Continuar','Sair']

    limpaTela()
    print(" CAMPO MINADO ","\n\n")
    print(" MENU ","\n")
    for i, v in enumerate(listaMenu):
        print(i+1, v,"\n\n")

    opcao = input("Escolha uma opcao: ")
    if(opcao == '1'):
        novoJogo(conexao)
    elif(opcao == '2'):
        carregar_Jogo(conexao)
    else:
        sys.exit(0)

""" ***********************************************
    Inicia o jogo chamando a funcao do Menu e 
    a partir dela resolve as demais pendencias.
********************************************** """
Menu()
