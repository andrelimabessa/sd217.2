import socket
from datetime import datetime

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
        text = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        print(address, text)

        #Envia resposta
        text = "Total de dados recebidos: " + str(len(data)) 
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

server()