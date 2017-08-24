""" """
from random import randint


class CampoMinado(object):
    def __init__(self, tamanho):
        """" Inicializando o objeto com tabuleiro tamanhoXtamanho"""
        self.tamanho = tamanho
        self.quantidade_bombas = self.__total_bombas()
        self.__distribuir_bombas()
        self.coordenadas_bombas = []
        self.tabuleiro = [[0 for j in range(tamanho)] for i in range(tamanho)]

    def __total_bombas(self):
        return self.tamanho / 2

    def __distribuir_bombas(self):
        quantidadade_bombas = self.quantidade_bombas
        while quantidadade_bombas > 0:
            coordenada = (randint(0, self.tamanho), randint(0, self.tamanho))
            if coordenada not in self.coordenadas_bombas:
                self.coordenadas_bombas


    def __str__(self):
        return str(self.tabuleiro)

    def _teste_(self):
        self.__distribuir_bombas()


objecto = CampoMinado()
print(objecto)
