import socket
from datetime import datetime
from campo_minado_negocio import CampoMinado
from ast import literal_eval
ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor



def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        resposta = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        resposta = tratar_mensagem(mensagem)
        print(address, mensagem)


        
        #Envia resposta
        resposta = "Total de dados recebidos: " + str(len(data))
        data = resposta.encode(ENCODE) # Codifica para BASE64 os dados
        sock.sendto(data, address) # Enviando dados


objeto = CampoMinado()
def criar_novo_jogo(contexto):
    linha = conrespostao["linha"]
    coluna = conrespostao["coluna"]
    objeto.criar_novo_jogo(linha,coluna)

def tratar_mensagem(mensagem):
    conrespostao = literal_eval(mensagem)
    codigo = conrespostao["codigo_comando"]
    switch = {
        "1":criar_novo_jogo
    }
    func = switch[codigo]
    func[contexto]

#INICIAR
server()
