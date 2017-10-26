from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from src.Monolitico.campo_minado_negocio import CampoMinado

OK = "200"

campo_minado = CampoMinado()


def criar_novo_jogo(linhas,colunas):
    global campo_minado
    campo_minado.criar_novo_jogo(linhas, colunas)
    return OK


def efetuar_jogada(linha, coluna):
    return campo_minado.jogada(linha, coluna)


def jogadas_restantes():
    return campo_minado.jogadas_restantes


def retorna_tabuleiro():
    global campo_minado
    return campo_minado.retornar_tabuleiro()


def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_novo_jogo)
    serverRPC.register_function(efetuar_jogada)
    serverRPC.register_function(jogadas_restantes)
    serverRPC.register_function(retorna_tabuleiro)
    print("Starting server")
    serverRPC.serve_forever()
