import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    #necessário colocar o prefixo exposed_ para o método line_counter ser visivel de maneira remota
    def exposed_line_counter(self, fileobj, function): 
        print('Cliente chamou line counter')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    #necessário colocar o prefixo exposed_ para o método print_name ser visivel de maneira remota
    def exposed_print_name(self, nome, sobrenome):
        return nome + " " + sobrenome

def server():    
    t = ThreadedServer(MyService, port = 18861)
    t.start()
