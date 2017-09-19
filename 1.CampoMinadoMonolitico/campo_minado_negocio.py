# -*- coding: utf-8 -*-
from random import randint
from sys import exit
from os import remove
from os.path import isfile
import constants
import json


class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha, coluna)

    def __inicializar_tabuleiro(self, linha, coluna):
        return [['X' for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas -= 1
        return coordenadas_bombas

    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def imprimir_tabuleiro(self):
        print "-" * 30
        for posicao in self.__tabuleiro:
            print ', '.join(map(str, posicao))
        print "-" * 30

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
            indexes_to_remove = [
                (line - 1, column - 1),
                (line - 1, column),
                (line - 1, column + 1),
            ]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]
        elif line == self.__linha - 1:
            indexes_to_remove = [
                (line + 1, column - 1),
                (line + 1, column),
                (line + 1, column + 1)
            ]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]

        # Eliminating adjacent coordinates from special cases
        if column == 0:
            indexes_to_remove = [
                (line, column - 1),
                (line - 1, column - 1),
                (line + 1, column - 1),
            ]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]
        elif column == self.__coluna - 1:
            indexes_to_remove = [
                (line, column + 1),
                (line - 1, column + 1),
                (line + 1, column + 1)
            ]
            adjacent_coordinates = [v for i, v in enumerate(adjacent_coordinates) if i not in indexes_to_remove]

        for coordinate in adjacent_coordinates:

            if coordinate in self.__coordenadas_bombas:
                adjacent_bombs_quantity += 1

        return adjacent_bombs_quantity

    def __store(self):

        game = {
            'linha': self.__linha,
            'coluna': self.__coluna,
            'tabuleiro': self.__tabuleiro,
            'coordenadas_bombas': self.__coordenadas_bombas
        }
        game_file = open(constants.game_file_name, 'w')

        game_file.write(json.dumps(game))
        game_file.close()

    def __delete(self):
        if isfile(constants.game_file_name):
            remove(constants.game_file_name)

    def __end_game(self, message):
        print message
        self.__delete()
        exit(0)

    def restore(self, game):
        self.__linha = game['linha']
        self.__coluna = game['coluna']
        self.__tabuleiro = game['tabuleiro']
        self.__coordenadas_bombas = game['coordenadas_bombas']

    def jogada(self, linha, coluna):
        coordinate_to_play = [linha, coluna]

        if linha < 0 or coluna < 0:
            print "This coordinate(%r, %r) isn't valid." % tuple(coordinate_to_play)
            return
        elif linha >= self.__linha or coluna >= self.__coluna:
            print "This coordinate(%r, %r) doesn't exist in the board." % tuple(coordinate_to_play)
            return

        if coordinate_to_play in self.__coordenadas_bombas:
            self.__end_game("You hit a bomb!")
        else:
            self.__tabuleiro[linha][coluna] = self.__get_adjacent_bombs_quantity__(linha, coluna)
            hidden_pieces = 0
            bombs_size = len(self.__coordenadas_bombas)

            for line in self.__tabuleiro:
                hidden_pieces += len(filter(lambda item: item == 'X', line))

            if hidden_pieces == bombs_size:
                self.__end_game("Congratulations!!!")
            else:
                self.__store()
