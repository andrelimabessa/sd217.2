import rpyc
from rpyc.utils.server import ThreadedServer
from campo_minado_negocio import CampoMinado

class MyService(rpyc.Service):
    objeto=""
    """ Funcap para iniciar um jogo novo. Imprimindo algumas informacoes. """
    def exposed_novo_jogo(self,linMax,colMax):
        print("Criando Novo Jogo!!")
        print("Total de Linhas e Colunas: ",linMax, colMax)
        global objeto
        objeto=CampoMinado(linMax,colMax)
        totBombas = objeto.total_bombas()
        tabuleiro = objeto.retorna_tabuleiro()
        if(linMax != 0):
            resposta = {'totalBombas':totBombas}
        else:
            linhaColuna = objeto.linhaColuna()
            resposta = {'totalBombas':totBombas,'linha':linhaColuna['linha'],'coluna':linhaColuna['coluna']}

        return resposta

    """ Funcao para retornar o tabuleiro para impressao """
    def exposed_retorna_tabuleiro(self):
        global objeto
        resposta=objeto.retorna_tabuleiro()
        return resposta

    """ Funcao para avaliar a jogada """
    def exposed_jogada(self,linha,coluna):
        global objeto
        resposta=objeto.jogada(linha,coluna)
        return resposta

    """ Funcao para gerar e imprimir a matriz final pos-derrota """
    def exposed_matriz_bomba(self,board):
        global objeto
        resposta=objeto.matriz_bomba(board)
        return resposta

    """ Funcao de inicio do servidor nao utilizada por enquanto """
    def server():
        t = ThreadedServer(MyService, port = 9999)
        t.start()


""" Iniciando o servidor """
if __name__ == "__main__":
    print("Iniciado o servidor")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 9999)
    t.start()
