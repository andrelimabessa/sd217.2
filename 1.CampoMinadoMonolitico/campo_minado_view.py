from campo_minado_negocio import CampoMinado

objeto = CampoMinado(3, 5)
objeto.imprimir_tabuleiro()

#objeto.menu()


while objeto.proxima_jogada():
    print (objeto.proxima_jogada())

    linha = int(input("Entre com posicao da linha :"))
    coluna = int(input("Entre com posicao da coluna :")) #input("Entre com posicao da coluna :")

    objeto.jogada(linha,coluna)


objeto.imprimir_tabuleiro()

""" 1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitoria

    4. Salvar jogadas
    5.Continuar jogo"""
