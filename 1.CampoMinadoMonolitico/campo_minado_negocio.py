# -*- coding: utf-8 -*-
from random import randint
from sys import exit

class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha__ = linha
        self.__coluna__ = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)


    def __inicializar_tabuleiro(self, linha, coluna):
        return [['X' for x in range(coluna)] for j in range(linha)]


    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas__(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        return coordenadas_bombas


    def __total_bombas__(self, linha, coluna):
        return int((linha*coluna)/3)


    def imprimir_tabuleiro(self):
        print "-" * 50
        for posicao in self.__tabuleiro:
            print(str(posicao))
        print "-" * 50


    def __get_adjacent_bombs_quantity__(self, line, column):
        adjacent_bombs_quantity = 0
        adjacent_coordinates = [
            (line, column - 1),
            (line, column + 1),
            (line - 1, column - 1),
            (line - 1, column),
            (line - 1, column + 1),
            (line + 1, column - 1),
            (line + 1, column),
            (line + 1, column + 1)
        ]

        # Eliminating adjacent coordinates from special cases
        if line == 0:
            indexes_to_remove = [2, 3, 4]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]
        elif line == self.__linha__ - 1:
            indexes_to_remove = [5, 6, 7]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]

        # Eliminating adjacent coordinates from special cases
        if column == 0:
            indexes_to_remove = [0, 2, 5]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]
        elif column == self.__coluna__ - 1:
            indexes_to_remove = [1, 4, 7]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]

        for coordinate in adjacent_coordinates:

            if coordinate in self.__coordenadas_bombas:
                adjacent_bombs_quantity += 1

        return adjacent_bombs_quantity


    def jogada(self, linha, coluna):
        coordinate_to_play = (linha, coluna)

        if linha < 0 or coluna < 0:
            print "This coordinate(%r, %r) isn't valid." % coordinate_to_play
            return
        elif linha >= self.__linha__ or coluna >= self.__coluna__:
            print "This coordinate(%r, %r) doesn't exist in the board." % coordinate_to_play
            return

        if coordinate_to_play in self.__coordenadas_bombas:
            print "You hit a bomb!"
            exit(0)
        else:
            self.__tabuleiro[linha][coluna] = self.__get_adjacent_bombs_quantity__(linha, coluna)
