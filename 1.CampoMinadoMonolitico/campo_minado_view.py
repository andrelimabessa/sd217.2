# -*- coding: utf-8 -*-
from os.path import isfile
from os import remove
import json
import subprocess as sp

import constants
import util
from campo_minado_negocio import CampoMinado

minefield = CampoMinado(10, 10)


def run_match():
    line = raw_input("Which line do you want to play: ")
    column = raw_input("Which column do you want to play: ")

    if util.is_number(line) and util.is_number(column):
        sp.call('clear', shell=True)
        minefield.jogada(int(line), int(column))
        minefield.imprimir_tabuleiro()
    else:
        print "You should learn to type a number!"

    run_match()


def start_game():
    if isfile(constants.game_file_name):
        result = raw_input("There's an older game saved. Do you want to load?\n")
        if result == "yes":
            game_file = open(constants.game_file_name)
            game = json.loads(game_file.read())

            minefield.restore(game)
            game_file.close()
        else:
            remove(constants.game_file_name)

    run_match()


start_game()
