from random import randint

class CampoMinado:
    
    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.total_jogadas = (linha * coluna) - self.__total_bombas(linha, coluna)
        self.game_over = False
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

    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            print(str(posicao))

    def tamanho_tabuleiro(self):
        return self.__linha * self.__coluna

    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(0, self.__linha):
            print(self.__linha)
            print(self.__coluna)
            print("Linha invalida")
            return False
        elif coluna not in range(0, self.__coluna):
            print("Coluna invalida")
            return False
        return True

    def _contador_bombas(self, linha, coluna):
        bombas = 0
        for linha in range(linha - 1, linha + 1):
            for coluna in range(coluna - 1, coluna + 1):
                if (linha, coluna) in self.__coordenadas_bombas:
                    bombas += 1
        self.__tabuleiro[linha][coluna] = bombas
        for posicao in self.__tabuleiro:
            print(str(posicao))
        return bombas
  
    def jogada(self, linha, coluna):
        if self.__coordenadas_validas(linha, coluna):
            coordenada = linha, coluna
            print("Jogada")
            print("Linha: " + str(linha) + " Coluna: " + str(coluna))
            if coordenada in self.__coordenadas_bombas:
                self.total_jogadas = 0
                print("Game Over!")
                print("========================") 
                self.__game_over = True
                self.__init__(self.__linha, self.__coluna)
                self.imprimir_tabuleiro()
            else:
                if (self.total_jogadas == 0):
                    print("Game Won!")
                    self.__init__(self.__linha, self.__coluna)
                    self.imprimir_tabuleiro()
                else:
                    self.total_jogadas = self.total_jogadas - 1
                    print("========================")    
                    self._contador_bombas(linha, coluna)
                    print("========================")
                    print(self.total_jogadas)

   
