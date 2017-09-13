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
        total = 0

        for linha in range(linha - 1, linha + 1):
            for coluna in range(coluna - 1, coluna + 1):
                if (linha, coluna) in self.__coordenadas_bombas:
                    total += 1

        return total

    def __movimento(self, linha, coluna):
        total_bombas = self.__quantidade_bombas_vizinhas(linha, coluna)

        self.__tabuleiro[linha][coluna] = str(total_bombas)
        self.imprimir_tabuleiro()

    def jogada(self, linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina: 
                caso sim:
                    Game Over 
                caso não: 
                    marcar a posição escolhida no tabuleiro com a quantidade de 
                    bombas existentes nos nós vizinhos """
        if self.__coordenadas_validas(linha, coluna):
            if (linha, coluna) in self.__coordenadas_bombas:
                print("Game Over!")
            else:
                self.__movimento(linha, coluna)
            

