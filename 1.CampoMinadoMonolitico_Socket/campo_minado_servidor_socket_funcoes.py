import socket
from campo_minado_negocio import CampoMinado
from ast import literal_eval

HOST = '127.0.0.1'
PORT = 9999

""" Iniciando e aguardando por conexoes """
conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexao.bind((HOST, PORT))
conexao.listen(2)

conn, addr = conexao.accept()
print("Conectado: ", addr)

objeto = ""

""" Processando as mensagens do cliente """
try:
    while True:
        """ Mensagem do Cliente """
        objetoConR = conn.recv(1024).decode()
        """ Avaliando a Mensagem do Cliente para uso """
        mensagem = literal_eval(objetoConR)
        """ Caso Novo Jogo """
        if(mensagem['tipo'] == 'novoJogo'):
            print("Criando novo Jogo")
            resposta = novoJogo(mensagem,objeto)
            conn.sendall(str(resposta).encode())
        """ Processamento do Tabuleiro para impressao """
        elif(mensagem['tipo'] == 'retorna_tabuleiro'):
            tabuleiro = objeto.retorna_tabuleiro()
            resposta = str(tabuleiro)
            conn.sendall(str(tabuleiro).encode())
        """ Processando jogada do Cliente """
        elif(mensagem['tipo'] == 'jogada'):
            resposta = jogada(mensagem,objeto)
            conn.sendall(str(resposta).encode())
        """ Processando Matriz Final pos Derrota """
        elif(mensagem['tipo'] == 'matriz_bomba'):
            objetoConS = objeto.matriz_bomba(mensagem['board'])
            conn.sendall(str(objetoConS).encode())
except:
    conexao.close()
    
""" Funcao de Novo Jogo """
def novoJogo(mensagem,objeto):
    linMax = mensagem['linMax']
    colMax = mensagem['colMax']
    print(mensagem)
    objeto = CampoMinado(linMax,colMax)
    print(objeto)
    totBombas = objeto.total_bombas()
    tabuleiro = objeto.retorna_tabuleiro()
    if(linMax != 0):
        objetoConS = {'totalBombas':totBombas}
        print(objetoConS)
    else:                
        linhaColuna = objeto.linhaColuna()
        objetoConS = {'totalBombas':totBombas,'linha':linhaColuna['linha'],'coluna':linhaColuna['coluna']}
    
    return objetoConS

""" Funcao de Processamento da Jogada do Cliente """
def jogada(mensagem,objeto):
    lin = mensagem['linha']
    col = mensagem['coluna']
    objetoConS = objeto.jogada(lin,col)
    return objetoConS


