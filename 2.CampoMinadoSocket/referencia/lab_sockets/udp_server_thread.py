# coding: utf-8
import socket
import threading
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o servidor escuta
HOST = ''              # Endereco IP do Servidor

""" Forma Procedural """
def server_thread_procedural():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        # Criação de thread procedural
        t = threading.Thread(target=tratar_conexao, args=tuple([sock, data, address]))
        t.start()

def tratar_conexao(sock, data, address):
    text = data.decode(ENCODE)
    print(text)
    #Envia resposta
    text = "Quantidade de bytes enviados: " + str(len(data))
    data = text.encode(ENCODE)
    sock.sendto(data, address)

#####################################################################################################

""" Forma Orientado a objeto """
def server_thread_oo():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
 
        #Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address)
        tratador.start()

class ThreadTratador(threading.Thread):

    def __init__(self, sock, data, address):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.address = address

    def run(self):
        self.__tratar_conexao(self.sock, self.data, self.address)

    def __tratar_conexao(self, sock, data, address):
        text = data.decode(ENCODE)
        print(text)
        #Envia resposta
        text = "Quantidade de bytes enviados: " + str(len(data))
        data = text.encode(ENCODE)
        sock.sendto(data, address)


