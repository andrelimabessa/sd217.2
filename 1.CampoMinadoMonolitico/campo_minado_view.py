# -*- coding: utf-8 -*-
from os.path import isfile
import json
import subprocess as sp

import constants
import util
from campo_minado_negocio import CampoMinado

campo_minado = CampoMinado(10, 10)
# objeto.imprimir_tabuleiro()
# objeto.jogada(9, 9)
# objeto.imprimir_tabuleiro()




def run_match():
    line = raw_input("Which line do you want to play: ")
    column = raw_input("Which column do you want to play: ")

    if util.is_number(line) and util.is_number(column):
        sp.call('clear', shell=True)
        campo_minado.jogada(int(line), int(column))
        campo_minado.imprimir_tabuleiro()
    else:
        print "You should learn to type a number!"

    run_match()


def start_game():
    if isfile(constants.game_file_name):
        result = raw_input("There's an older game saved. Do you want to load?\n")
        if result == "yes":
            game_file = open(constants.game_file_name)
            game = json.loads(game_file.read())

            campo_minado.restore(game)
            game_file.close()

    run_match()


start_game()
