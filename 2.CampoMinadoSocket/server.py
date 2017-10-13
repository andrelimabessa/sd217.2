import socket
from datetime import datetime
from ast import literal_eval
from campo_minado_negocio import CampoMinado
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_FALHA, RESPOSTA_SUCESSO

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor

def servidor():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    
    #Cria uma instância para o jogo campo minado
    jogo = CampoMinado()

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        mensagem = data.decode(ENCODE)           # Convertendo dados de BASE64 para UTF-8
        contexto = literal_eval(mensagem)

        #Trata comando recebido por algum cliente
        resposta = tratar_mensagem(jogo, contexto)
        print(address, mensagem)

        #Envia resposta
        data = resposta.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

def tratar_mensagem(jogo, contexto):

    codigo = contexto["codigo_comando"]

    switch = {
       "1": criar_novo_jogo 
    }
    func = switch.get(str(codigo))
    
    #Todas as funções devem receber 
    return func(jogo, contexto)

def criar_novo_jogo(jogo,contexto):

    linha = int(contexto.get(QUANTIDADE_LINHAS))
    coluna = int(contexto.get(QUANTIDADE_COLUNAS))
    jogo.criar_novo_jogo(linha,coluna)
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

if __name__ == "__main__":
    servidor()
