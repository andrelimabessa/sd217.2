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

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(0,self.__linha):
            print("Linha Invalida")
            return False
        elif linha not in range(0,self.__coluna):
            print("Coluna Invalida")
            return False
        else:
            return True
    def __mina_acertada(self, linha, coluna):
        coordenada = (linha,coluna)
        if coordenada  in self.__coordenadas_bombas:
            return True
        return False

        

    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

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
        if self.__coordenadas_validas(linha,coluna):
            if self.__mina_acertada(linha,coluna):
                print("Game Over")
            else:
                print("Escapou Fedendo !!")
            
       # raise NotImplementedError("Método não implementado")

