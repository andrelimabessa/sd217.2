from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def print_name(nome, sobrenome):
    """ Concatena nome mais sobrenome"""
    return nome + " " + sobrenome

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(print_name)
    print("Starting server")
    serverRPC.serve_forever()
