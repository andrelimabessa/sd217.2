from random import randint
from .models import Jogada

class CampoMinado:
    __linha = 0
    __coluna = 0
    __tabuleiro = []
    __posicao = []

    def __init__(self, linha, coluna):
        self.__linha = int(linha)
        self.__coluna = int(coluna)
        self.__tabuleiro = [['X' for x in range(self.__coluna)] for j in range(self.__linha)]

    def get(self):
        for i in range(0, 3):
            linha = randint(0, self.__linha-1)
            coluna = randint(0, self.__coluna-1)
            self.__tabuleiro[linha][coluna] = "bomba"
        return self.__tabuleiro
