import zmq
import time
import sys
import random

try:
    port = "5560"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:%s" % port)
    server_id = random.randrange(1,10005)
    while True:
        #  Espera pela próxima requisição do cliente
        message = socket.recv()
        print("Recebi requisição de : ", message)
        time.sleep (1)
        text = "Id do servidor %s" % server_id
        data = text.encode("UTF-8")
        socket.send(data)
except:
    for val in sys.exc_info():
        print(val)

input("Saida Enter")
