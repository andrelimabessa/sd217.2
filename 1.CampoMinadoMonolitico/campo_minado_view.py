from campo_minado_negocio import CampoMinado

objeto = CampoMinado(4, 4)
print("Bom Jogo!")
objeto.imprimir_tabuleiro()
num_jogadas = 0
game_won = False

print(objeto.total_jogadas)

tamanho = objeto.tamanho_tabuleiro()

num_jogadas_max  = tamanho
while objeto.total_jogadas > 0:
    line = int(input("Digite uma linha: "))
    col = int(input("Digite uma coluna: "))
    print("Linha: " + str(line) + "\nColuna: " + str(col))
    objeto.jogada(line, col)
    if num_jogadas_max == 0:
        game_won = True
        game_over = True
        print("Game Won!")
        break
    if objeto.game_over == True and game_won == False:
        print("========================")
        print("Game Over!")
        print("*****Novo Jogo*****")


