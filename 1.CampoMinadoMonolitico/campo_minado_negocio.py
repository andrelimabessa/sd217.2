from random import randint

class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)
        
    def __inicializar_tabuleiro(self, linha, coluna):
        
        board = [['X' for x in range(coluna)] for j in range(linha)]
        for l in range(linha):
            for c in range(coluna):
                if l != 0 and c != 0:
                    board[l][c] = 'X'
                elif l == 0 and c != 0:
                    board[l][c] = str(c)
                elif l != 0 and c == 0:
                    board[l][c] = str(l)
                else:
                    board[0][0] = ' '
                    
        return board

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 1:
            coordenada = (randint(1, linha - 1), randint(1, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        """ Adicionado por mim para testar uma bomba conhecida """        
        coordenada = (1,1)
        coordenadas_bombas.append(coordenada)
        return coordenadas_bombas

    def __total_bombas(self, linha, coluna):
        return int((linha-1*coluna-1)/3)

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(1,self.__linha):
            print("Linha Invalida")
            return False
        elif coluna not in range(1,self.__coluna):
            print("Coluna Invalida")
            return False
        return True

    def __conta_bombas_vizinho(self, linha, coluna):
        pass

    def __jogada_result(self, linha, coluna):
        cont = 0
        for l in range(linha-1,linha+1):
            for c in range(coluna-1,coluna+1): 
                posicao = (l,c)
                if posicao in self.__coordenadas_bombas:
                    cont += 1
            
        self.__tabuleiro[linha][coluna] = str(cont)
                
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
                    
            posicao = (linha,coluna)
            if posicao in self.__coordenadas_bombas:
                print("Fim de jogo!!")
            else:
                self.__jogada_result(linha,coluna)
