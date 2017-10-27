import socket
from datetime import datetime
from ast import literal_eval
from os.path import isfile
from os import remove
import json
from campo_minado_negocio import CampoMinado
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_FALHA, RESPOSTA_SUCESSO ,JOGADA_COLUNA, JOGADA_LINHA , CODIGO_COMANDO, COMANDO_EFETUAR_JOGADA, COMANDO_SHOW, IMPRIMIR, QTD

def servidor():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_novo_jogo)

    # serverRPC.register_function(criar_novo_jogo)
    # serverRPC.register_function(efetuar_jogada)
    # serverRPC.register_function(jogadas_restantes)
    # serverRPC.register_function(retorna_tabuleiro)
    print("Starting server")
    serverRPC.serve_forever()


# def tratar_mensagem(jogo, contexto):
#
#     codigo = contexto["codigo_comando"]
#     #print("CODIGO =  ",codigo)
#     switch = {
#        "1": criar_novo_jogo,
#        "2": restaurar_jogo,
#        "efetuar_jogada":jogada,
#        "jogadas":quatidade,
#        "tabuleiro":tabuleiro_show
#     }
#     func = switch.get(str(codigo))
#     print("IMPRIMIR CONTEXTO ",contexto)
#     #Todas as funções devem receber
#     return func(jogo, contexto)


def tabuleiro_show(jogo,contexto):
    tabuleiro = jogo.tabuleiro_show()
    return str(tabuleiro)

def quatidade(jogo,contexto):
    jogadas = jogo.qtd_jogadas()
    return str(jogadas)


def jogada(jogo,contexto):
    #print("JOGADA() CONTEXTO  ", contexto)
    linha = int(contexto.get(JOGADA_LINHA))
    coluna = int(contexto.get(JOGADA_COLUNA))
    #print("LINHA ",linha," COLUNA ",coluna)
    jogo.jogada(linha,coluna)
    #jogadas = jogo.qtd_jogadas()
    #resposta = [tabuleiro]
    # resposta[1] = jogadas
    #tabuleiro = jogo.tabuleiro_show()
    #return str(tabuleiro)
    #return (str(tabuleiro),str(jogadas))
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

def restaurar_jogo(jogo,contexto):
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        jogo.restaurar(game)
        arquivo.close()

def criar_novo_jogo(jogo,contexto):

    linha = int(contexto.get(QUANTIDADE_LINHAS))
    coluna = int(contexto.get(QUANTIDADE_COLUNAS))

    #print(linha,coluna)
    jogo.criar_novo_jogo(linha,coluna)
    jogo.tabuleiro_show()
    tabu = jogo.tabuleiro_show()
    #print (tabu)


    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

if __name__ == "__main__":
    servidor()
