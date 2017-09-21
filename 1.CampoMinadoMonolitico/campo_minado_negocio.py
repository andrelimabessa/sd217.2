from random import randint
from ast import literal_eval
import os
class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self._qtd_jogadas = (linha * coluna) - self.__total_bombas(linha, coluna)
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)

    def __inicializar_tabuleiro(self, linha, coluna):
        return [['*' for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        return coordenadas_bombas

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(0,self.__linha):
            print("Linha Invalida")
            return False
        elif linha not in range(0,self.__coluna):
            print("Coluna Invalida")
            return False
        else:
            return True
    def __mina_acertada(self, linha, coluna):
        coordenada = (linha,coluna)
        if coordenada  in self.__coordenadas_bombas:
            return True
        return False
    def __menu(self):
        print(". . . .  . . . . . . .Campo Minado . . . . . . .  . . . .")
        print(". . . . @ . . . . . . . . . . . . . . @ . . . .")





    def __pega_vizinhos(self,linha,coluna):
        coordenada = (linha,coluna)
        linhaLESQ = linha - 1
        linhaLDIR = linha + 1
        linhaCAC = coluna - 1
        linhaCAB = coluna + 1
        coordenada1 = (linhaLESQ,coluna)
        coordenada2 = (linhaLDIR,coluna)
        coordenada3 = (linha,linhaCAC)
        coordenada4 = (linha,linhaCAB)
        vizinhos = []
        count = 0

        if coordenada1 in self.__coordenadas_bombas :
            count = count + 1

        elif coordenada2 in self.__coordenadas_bombas :
            count =  + 1

        elif coordenada3 in self.__coordenadas_bombas :
            count = count + 1

        elif coordenada4 in self.__coordenadas_bombas :
            count = count + 1


        else:
            pass

        return count







    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def imprimir_tabuleiro(self):

        for posicao in self.__tabuleiro:
            print(str(posicao))

    def proxima_jogada(self):
        return self._qtd_jogadas > 0


    def perdeu(self):
        print("______________MINA ACERTADA____________________")
        print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
        print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
        print(". . . . . @ BOOM!!! ÉRROOOUU ! Fastop ! @ . .. . . ")
        print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
        print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
        print("_________________________________________________\n\n")

    def jogada(self,linha,coluna):


        if self.__coordenadas_validas(linha,coluna):
            if self.__mina_acertada(linha,coluna):
                self.perdeu()
                self.__tabuleiro[linha][coluna] = 0

                self._qtd_jogadas = 0


            else:
                print("Escapou Fedendo !!")
                print("Jogadas faltando: " + str(self._qtd_jogadas))
                self.__tabuleiro[linha][coluna] = self.__pega_vizinhos(linha,coluna)
                self._qtd_jogadas-=1



       # raise NotImplementedError("Método não implementado")
