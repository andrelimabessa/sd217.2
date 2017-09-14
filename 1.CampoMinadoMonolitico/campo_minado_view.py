from campo_minado_negocio import CampoMinado
import os
"""objeto = CampoMinado(10, 10)"""
"""objeto.imprimir_tabuleiro()"""
"""objeto.jogada(9,9)"""
"""objeto.imprimir_tabuleiro()"""
jogar = True
while(jogar):
    unused_variable = os.system("clear")
    linMax = int(input("Digite o total de linhas: "))
    colMax = int(input("Digite o total de colunas: "))
    objeto = CampoMinado(linMax,colMax)
    jogar = objeto.principal()
    



