import zmq
from campo_minado_negocio import CampoMinado
from ast import literal_eval

PORT = "5560"

""" Iniciando e aguardando por conexoes """
context = zmq.Context()
conn = context.socket(zmq.REP)
conn.connect("tcp://localhost:%s" % PORT)

print("Conectado: ")

objeto = CampoMinado

""" Funcao de Novo Jogo """
def novoJogo(mensagem,objeto):
    linMax = mensagem['linMax']
    colMax = mensagem['colMax']
    print(mensagem)
    objeto = CampoMinado(linMax,colMax)
    print(objeto)
    totBombas = objeto.total_bombas()
    if(linMax != 0):
        objetoConS = {'totalBombas':totBombas}
        print(objetoConS)
    else:
        linhaColuna = objeto.linhaColuna()
        objetoConS = {'totalBombas':totBombas,'linha':linhaColuna['linha'],'coluna':linhaColuna['coluna']}
    
    objeto.salvarJogo()
    return objetoConS

""" Funcao de Processamento da Jogada do Cliente """
def jogada(mensagem,objeto):
    lin = mensagem['linha']
    col = mensagem['coluna']
    objetoConS = objeto.jogada(lin,col)
    return objetoConS

""" Processando as mensagens do cliente """

while True:
    """ Mensagem do Cliente """
    objetoConR = conn.recv().decode()
    """ Avaliando a Mensagem do Cliente para uso """
    mensagem = literal_eval(objetoConR)
    print(mensagem)
    """ Caso Novo Jogo """
    if(mensagem['tipo'] == 'novoJogo'):
        print("Criando novo Jogo")
        resposta = novoJogo(mensagem,objeto)    
        conn.send(str(resposta).encode())

    """ Processamento do Tabuleiro para impressao """
    if(mensagem['tipo'] == 'retorna_tabuleiro'):
        print("Impressao do Tabuleiro")
        objeto = CampoMinado
        tabuleiro = objeto.retornaTabuleiro()
        print(tabuleiro)
        resposta = str(tabuleiro)
        conn.send(resposta.encode())

    """ Processando jogada do Cliente """
    if(mensagem['tipo'] == 'jogada'):
        objeto = CampoMinado(0,0)
        resposta = jogada(mensagem,objeto)
        conn.send(str(resposta).encode())

    """ Processando Matriz Final pos Derrota """
    if(mensagem['tipo'] == 'matriz_bomba'):
        objetoConS = objeto.matriz_bomba(mensagem['board'])
        conn.send(str(objetoConS).encode())
