from campo_minado_negocio import CampoMinado

objeto = CampoMinado(3, 5)


#objeto.menu()


while objeto.proxima_jogada():
    #print (objeto.proxima_jogada())
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - SAIR                               #")
    print("#########################################\n")

    op = int(input("Inserir Opção :"))
    
    objeto.imprimir_tabuleiro()

    linha = int(input("Entre com posicao da linha :"))
    coluna = int(input("Entre com posicao da coluna :")) #input("Entre com posicao da coluna :")

    objeto.jogada(linha,coluna)


objeto.imprimir_tabuleiro()

""" 1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitoria

    4. Salvar jogadas
    5.Continuar jogo"""
