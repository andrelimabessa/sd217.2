""" ****************************************
    Modelo Alternativo de Servidor sem o uso
    das funcaoes NovoJogo e Jogada. Os comentarios
    sao os mesmos da versao com Funcoes.
*****************************************"""
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

""" Processando as mensagens do cliente """
try:
    while True:
        objetoConR = conn.recv(1024).decode()
        mensagem = literal_eval(objetoConR)
        if(mensagem['tipo'] == 'novoJogo'):
            linMax = mensagem['linMax']
            colMax = mensagem['colMax']
            objeto = CampoMinado(linMax,colMax)
            totBombas = objeto.total_bombas()
            tabuleiro = objeto.retorna_tabuleiro()
            if(linMax != 0):
                objetoConS = {'totalBombas':totBombas}
            else:                
                linhaColuna = objeto.linhaColuna()
                objetoConS = {'totalBombas':totBombas,'linha':linhaColuna['linha'],'coluna':linhaColuna['coluna']}

            resposta = str(objetoConS)
            conn.sendall(str(objetoConS).encode())
        elif(mensagem['tipo'] == 'retorna_tabuleiro'):
            tabuleiro = objeto.retorna_tabuleiro()
            resposta = str(tabuleiro)
            conn.sendall(str(tabuleiro).encode())
        elif(mensagem['tipo'] == 'jogada'):
            lin = mensagem['linha']
            col = mensagem['coluna']
            objetoConS = objeto.jogada(lin,col)
            resposta = str(objetoConS)
            conn.sendall(str(objetoConS).encode())
        elif(mensagem['tipo'] == 'continuar'):
            linMax = mensagem['linMax']
            colMax = mensagem['colMax']
            objeto = CampoMinado(linMax,colMax)
            objetoConS = objeto.carregarJogo()
            conn.sendall(str(objetoConS).encode())
        elif(mensagem['tipo'] == 'matriz_bomba'):
            objetoConS = objeto.matriz_bomba(mensagem['board'])
            resposta = str(objetoConS)
            conn.sendall(str(objetoConS).encode())
except:
    conexao.close()



    
