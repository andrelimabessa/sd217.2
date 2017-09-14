from random import randint


class CampoMinado:
    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha, coluna)

    def __inicializar_tabuleiro(self, linha, coluna):
        # return [[str(x) + "," + str(j) for x in range(coluna)] for j in range(linha)]
        return [["X" for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas -= 1
        return coordenadas_bombas

    def __total_bombas(self, linha, coluna):
        return int((linha * coluna) / 3)

    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            print(str(posicao))

    def jogada(self, linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina: 
                caso sim:
                    Game Over 
                caso não: 
                    marcar a posição escolhida no tabuleiro com a quantidade de 
                    bombas existentes nos nós vizinhos """

        if linha not in range(self.__linha):
            print("Linha invalida.")
        elif coluna not in range(self.__coluna):
            print("Coluna invalida.")
        elif self.procurar_bomba(coluna, linha):
            print("Você morreu!")
        else:
            self.marcar_posicao(linha, coluna, self.contar_bombas_adjacentes(linha, coluna))
            self.imprimir_tabuleiro()


    def procurar_bomba(self, coluna, linha):
        return (linha, coluna) in self.__coordenadas_bombas

    def contar_bombas_adjacentes(self, linha, coluna):
        linha_adjacente = linha - 1
        total_bombas = 0
        while linha_adjacente <= linha + 1:
            coluna_adjacente = coluna - 1
            while coluna_adjacente <= coluna + 1:
                if self.procurar_bomba(linha_adjacente, coluna_adjacente):
                    total_bombas += 1
                coluna_adjacente+=1
            linha_adjacente+=1
        print(str(total_bombas))
        return total_bombas

    def marcar_posicao(self, linha, coluna, quantidade_bombas):
        self.__tabuleiro[linha][coluna] = str(quantidade_bombas)
