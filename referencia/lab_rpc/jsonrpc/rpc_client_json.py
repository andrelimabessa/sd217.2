from jsonrpclib import Server

def client():
    proxy = Server('http://localhost:7002')
    print(proxy.print_name("André", "Bessa"))
