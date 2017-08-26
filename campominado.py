from random import randint

class CampoMinado:

    def __init__(self, tamanho):
        """ Iniciando objeto com tabuleiro NxN """
        self.tamanho = tamanho
        self.coordenadas_bombas = []
        self.qtd_bombas = self.__total_bombas()
        self.__distribuir_bombas()
        self.tabuleiro = [['X' for i in range(tamanho)] for j in range(tamanho)]

    def __distribuir_bombas(self):
        num_bombas = self.qtd_bombas
        while num_bombas > 0:
            coordenada = (randint(0, self.tamanho),randint(0, self.tamanho))
            if coordenada not in self.coordenadas_bombas:
                self.coordenadas_bombas.append(coordenada)
                num_bombas-=1

        #print(str(randint(0, self.tamanho)))

    def __total_bombas(self):
        return self.tamanho/2

    def __str__(self):
        return str(self.tabuleiro)

o = CampoMinado(10)
for linha in o.tabuleiro:
    print(str(linha))

#print(o)