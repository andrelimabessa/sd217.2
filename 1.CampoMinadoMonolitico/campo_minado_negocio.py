from random import randint

class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)
        
    def __inicializar_tabuleiro(self, linha, coluna):
        return [['X' for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        return coordenadas_bombas

    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            print(str(posicao))

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(0, self.__linha):
            print("linha inválida")
            return False
        elif coluna not in range(0, self.__coluna):
            print("coluna inválida")
            return False
        return True

    def __quantidade_bombas_vizinhas(self, linha, coluna):
        bombas = 0
        coordenadas_bombas_vizinhas = [
            (linha, coluna - 1),
            (linha, coluna + 1),
            (linha - 1, coluna - 1),
            (linha - 1, coluna),
            (linha - 1, coluna + 1),
            (linha + 1, coluna - 1),
            (linha + 1, coluna),
            (linha + 1, coluna + 1)
        ]

        
        if linha == 0:
            indices = [
                (linha - 1, coluna - 1),
                (linha - 1, coluna),
                (linha - 1, coluna + 1),
            ]
            coordenadas_bombas_vizinhas = [v for i, v in enumerate(coordenadas_bombas_vizinhas) if i not in indices]
        elif linha == self.__linha - 1:
            indices = [
                (linha + 1, coluna - 1),
                (linha + 1, coluna),
                (linha + 1, coluna + 1)
            ]
            coordenadas_bombas_vizinhas = [v for i, v in enumerate(coordenadas_bombas_vizinhas) if i not in indices]

        if coluna == 0:
            indices = [
                (linha, coluna - 1),
                (linha - 1, coluna - 1),
                (linha + 1, coluna - 1),
            ]
            coordenadas_bombas_vizinhas = [v for i, v in enumerate(coordenadas_bombas_vizinhas) if i not in indices]
        elif coluna == self.__coluna - 1:
            indices = [
                (linha, coluna + 1),
                (linha - 1, coluna + 1),
                (linha + 1, coluna + 1)
            ]
            coordenadas_bombas_vizinhas = [v for i, v in enumerate(coordenadas_bombas_vizinhas) if i not in indices]

        for coordinate in coordenadas_bombas_vizinhas:

            if coordinate in self.__coordenadas_bombas:
                bombas += 1

        return bombas

    def __movimento(self, linha, coluna):
        total_bombas = self.__quantidade_bombas_vizinhas(linha, coluna)

        self.__tabuleiro[linha][coluna] = str(total_bombas)
        self.imprimir_tabuleiro()

    def jogada(self):
        jogada_linha = int(input("Insira a da linha jogada: ")) 
        jogada_coluna = int(input("Insira a da coluna jogada: ")) 
        if self.__coordenadas_validas(jogada_linha, jogada_coluna):
            if (jogada_linha, jogada_coluna) in self.__coordenadas_bombas:
                print("Game Over!")
            else:
                self.__movimento(jogada_linha, jogada_coluna)
                self.jogada()
            

