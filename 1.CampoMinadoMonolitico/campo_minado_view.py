from campo_minado_negocio import CampoMinado
import os
"""
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra para vitoria

    4. Salvar jogadas
    5. Continuar jogo
    
"""
jogar = True
while(jogar):
    unused_variable = os.system("clear")
    linMax = int(input("Digite o total de linhas: "))
    colMax = int(input("Digite o total de colunas: "))
    objeto = CampoMinado(linMax,colMax)
    jogar = objeto.principal()
    



