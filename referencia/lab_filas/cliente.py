import zmq
import sys
import random

port = "5559"
context = zmq.Context()
print("Conectando com o servidor...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)
client_id = random.randrange(1, 10005)
#  Envia 10 requisições
for request in range(1, 10):
    print("Enviando requisição ", request, "...")
    text = "Mensagem do cliente %s" % client_id
    data = text.encode("UTF-8")
    socket.send(data)
    #  Pega a resposta.
    message = socket.recv()
    print("Resposta recebida ", request, "[", message, "]")

input("Saida Enter")
