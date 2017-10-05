from jsonrpclib import Server

def client():
    proxy = Server('http://localhost:7002')
    print(proxy.printName("André", "Bessa"))
