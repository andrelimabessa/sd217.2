import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """

    text = input("Digite algum texto:\n")       # Recebe dados
    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    
    #Enviando de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
    dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
    sock.sendto(data, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor
    print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
    text = data.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8
    print(address, text)                        # Imprime texto e endereços

    #Fechando Socket
    sock.close()
    
client()