from campo_minado_negocio import CampoMinado

tamanho_campo = int(input("Digite o tamanho do campo: "))

objeto = CampoMinado(tamanho_campo, tamanho_campo)
objeto.imprimir_tabuleiro()
objeto.jogada()
