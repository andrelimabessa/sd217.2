from campo_minado_negocio import CampoMinado

objeto = CampoMinado(2,2)

def start():
    while objeto.proxima_jogada():
        objeto.imprimir_tabuleiro()
        linha = int(input("Entre com posicao da linha :"))
        coluna = int(input("Entre com posicao da coluna :"))
        objeto.jogada(linha,coluna)
        



def menu():
    print("#########################################")
    print("#              CAMPO MINADO             #")
    print("#########################################")
    print("#1 - INICIAR JOGO                       #")
    print("#2 - RESTAURAR                          #")
    print("#3 - SAIR                               #")
    print("#########################################\n")
    opcao = int(input("Inserir Opção :"))
    if opcao == 1:
        start()
    elif opcao == 2:
        pass
    else:
        pass

""" FIM MENU"""


menu()




""" 1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitoria

    4. Salvar jogadas
    5.Continuar jogo"""
