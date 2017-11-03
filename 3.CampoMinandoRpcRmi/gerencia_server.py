from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from campo_minado_negocio import CampoMinado
from os.path import isfile
import json
import sys

OK = "200"

campo_minado = CampoMinado()


def criar_novo_jogo(linhas,colunas):
    campo_minado.criar_novo_jogo(linhas, colunas)
    return OK


def efetuar_jogada(linha, coluna):
    return campo_minado.jogada(linha, coluna)

def total():
    return campo_minado.qtd_jogadas()

def jogadas_restantes():
    return campo_minado.qtd_jogadas()

def continuar():
    return campo_minado.proxima_jogada()

def restaurar_jogo():
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        campo_minado.restaurar(game)
        arquivo.close()

def retorna_tabuleiro():

    return campo_minado.tabuleiro_show()


def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_novo_jogo)
    serverRPC.register_function(efetuar_jogada)
    serverRPC.register_function(continuar)
    serverRPC.register_function(restaurar_jogo)
    serverRPC.register_function(jogadas_restantes)
    serverRPC.register_function(retorna_tabuleiro)
    print("Starting server")
    serverRPC.serve_forever()
