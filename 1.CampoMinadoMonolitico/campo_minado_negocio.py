from random import randint
import os
class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)
        
    def __inicializar_tabuleiro(self, linha, coluna):
        return [['*' for x in range(coluna)] for j in range(linha)]

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

    def __gameOver():
        print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
        print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
        print(". . . . . . @ BOOM!!! ÉRROOOUU ! Fastop ! @ . . . . . .")
        print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
        print(". . @ . . . . . . . . . . . . . . . . . . @ . .")

    def __pega_vizinhos(self,linha,coluna):
        coordenada = (linha,coluna)
        linhaLESQ = linha - 1
        linhaLDIR = linha + 1
        linhaCAC = coluna - 1
        linhaCAB = coluna + 1
        coordenada1 = (linhaLESQ,coluna)
        coordenada2 = (linhaLDIR,coluna)
        coordenada3 = (linha,linhaCAC)
        coordenada4 = (linha,linhaCAB)
        vizinhos = []
        count = 0

        if coordenada1 in self.__coordenadas_bombas :
            count = count + 1
            self.__tabuleiro[linhaLESQ][coluna] = 1
        elif coordenada2 in self.__coordenadas_bombas :
            count =  + 1
            self.__tabuleiro[linhaLDIR][coluna] = 1
        elif coordenada3 in self.__coordenadas_bombas :
            count = count + 1
            self.__tabuleiro[linha][linhaCAC] = 1
        elif coordenada4 in self.__coordenadas_bombas :
            count = count + 1
            self.__tabuleiro[linha][linhaCAB] = 1
        
        else:
            pass

        print ("Total bombas Vizinhas ",count )
        


        print (coordenada1)
        print (coordenada2)
        print (coordenada3)
        print (coordenada4)
        print (self.__coordenadas_bombas)
        #if coordenada in self.__coordenadas_bombas:
            #print ( coordenada[linha(-1)][coluna])

        #for 
        # for i in range(-1, 2):
        #     for j in range(-1, 2):
        #         if i == 0 and j == 0:
        #             countinue
        #         elif -1 < (linha + i) < tabuleiro and -1 < (coluna + j) < tabuleiro:
        #             vizinhos.append((linha + i, coluna + j))
        # return vizinhos

        

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
                os.system("cls")
                self.__pega_vizinhos(linha,coluna)
                self.__tabuleiro[linha][coluna] = 1
                print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
                print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
                print(". . . . . . @ BOOM!!! ÉRROOOUU ! Fastop ! @ . . . . . .")
                print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
                print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
                
                
            else:
                print("Escapou Fedendo !!")
                self.__tabuleiro[linha][coluna] = 0
            
       # raise NotImplementedError("Método não implementado")

