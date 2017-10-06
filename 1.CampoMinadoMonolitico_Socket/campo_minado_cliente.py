import socket

class MinhaConexao:

    def __init__(self):
        """ Endereco do Servidor e da Porta """
        HOST = '127.0.0.1'
        PORT = 9999
        """ Iniciando a conexao com o servidor e armazenando a mesma na variavel 'conexao' """
        try:
            conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexao.connect((HOST, PORT))
            return conexao
        except:
            
        
