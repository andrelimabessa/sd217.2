import sys
from jsonrpclib import Server
from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
import sys
#from campo_minado_view import iniciar_novo_jogo, continuar_jogo, efetuar_nova_jogada,menu_inicial, sair, restaurar_jogo
from consts_mensagem import CODIGO_COMANDO, CODIGO_RESPOSTA, COMANDO_EFETUAR_JOGADA, JOGADA_LINHA, JOGADA_COLUNA ,COMANDO_SHOW, IMPRIMIR, QTD,QUANTIDADE_LINHAS,QUANTIDADE_COLUNAS




proxy = Server('http://localhost:7002')
def enviar(mensagem):

    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    #Envio da mensagem
    data = mensagem.encode(ENCODE)
    sock.sendto(data, dest)

    #Receber resposta servidor
    data, address = sock.recvfrom(MAX_BYTES)
    respota = data.decode(ENCODE)

    #Fechando Socket
    sock.close()

    return respota

def client():
    proxy = Server('http://localhost:7002')


    #print(proxy.criar_novo_jogo(4,4))
    # proxy.criar_novo_jogo(4,4)
    # imprimir_tabuleiro(proxy.retorna_tabuleiro())


    # switcher = {
    #     1: iniciar_novo_jogo,
    #     9: sair,
    # }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))
        if opcao == 1 :
            contexto = {CODIGO_COMANDO: opcao}
            func(proxy.iniciar_novo_jogo())
        else:
            pass

        #func = switcher.get(opcao)

        print(func(proxy))
        tratar_jogadas()

        #contexto = {CODIGO_COMANDO: opcao}
        #print (contexto)


        #mensagem = func(contexto)
        #print(mensagem)
        #print(contexto)
        #resposta = literal_eval(enviar(mensagem))



def menu_inicial():
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")

"""Função para receber as jogadas e enviar para o servidor"""


def iniciar_novo_jogo():

    linha = int(input("Informe a qdssuantidade de linhas: "))
    coluna = int(input("Informe a quantidade de colunas: "))
    #str(con)
    return proxy.criar_novo_jogo(linha,coluna)
    #return str(contexto)


def sair(contexto):
    sys.exit(0)

def qtd_jogadas():
    contexto = {CODIGO_COMANDO: QTD}
    #tranforma em mensagem
    mensagem = str(contexto)
    #print("IMPRIMIR MSM !!!!!!!!!!" , mensagem)
    resposta = literal_eval(enviar(mensagem))
    return (str(resposta))

def tabuleiro_show():
    #contexto = {CODIGO_COMANDO: IMPRIMIR}
    #tranforma em mensagem
    mensagem = str(contexto)
    #print("IMPRIMIR MSM !!!!!!!!!!" , mensagem)
    resposta = literal_eval(enviar(mensagem))
    for posicao in resposta:
        print (str(posicao))

def tratar_jogadas():
    proxima_jogada = True
    while proxima_jogada:
        contexto = {CODIGO_COMANDO: COMANDO_EFETUAR_JOGADA}
        contexto[JOGADA_LINHA] = input("[Jogada] Informe a linha: ")
        contexto[JOGADA_COLUNA] = input("[Jogada] Informe a coluna: ")
        #tranforma em mensagem
        mensagem = str(contexto)
        #print("IMPRIMIR MSM" , mensagem)
        resposta = literal_eval(enviar(mensagem))  #resposta
        #print ((resposta))
        qtd = qtd_jogadas()
        print('QUANTIDADE DE JOGADAS RESTANTES',qtd)
        tabuleiro_show()
        if qtd == "0":
            print("GAMEOVER !")
            proxima_jogada = False
            #sys.exit(0)
            #False

"""Fim tratar_jogadas"""


if __name__ == "__main__":
    client()
