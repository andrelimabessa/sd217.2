from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
from campo_minado_view import iniciar_novo_jogo, continuar_jogo, efetuar_nova_jogada,menu_inicial, sair
from consts_mensagem import CODIGO_COMANDO, CODIGO_RESPOSTA

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def enviar(mensagem):

    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    #Envio da mensagem    
    data = mensagem.encode(ENCODE) 
    sock.sendto(data, dest)      

    #Receber resposta servidor
    data, address = sock.recvfrom(MAX_BYTES)   
    respota = data.decode(ENCODE)                  
     
    #Fechando Socket
    sock.close()

    return respota

def cliente():

    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))

        contexto = {CODIGO_COMANDO: opcao}
        
        func = switcher.get(opcao)

        mensagem = func(contexto)
        print(contexto)

        resposta = literal_eval(enviar(mensagem))
        print(resposta.get(CODIGO_RESPOSTA))

if __name__ == "__main__":
    cliente()