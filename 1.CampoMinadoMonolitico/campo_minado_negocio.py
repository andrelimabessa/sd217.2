from random import randint
import os

class CampoMinado:

    def __init__(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha + 1
        self.__coluna = coluna + 1
        self.__tabuleiro = self.__inicializar_tabuleiro(self.__linha,self.__coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(self.__linha,self.__coluna)
        self.__qtd_bombas = self.__total_bombas(self.__linha,self.__coluna)

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
                    board[l][c] = ' '

        return board

    def __distribuir_bombas(self, linha, coluna):
        quantidade_bombas = self.__total_bombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(1, linha-1), randint(1, coluna-1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1

        return coordenadas_bombas

    def __total_bombas(self, linha, coluna):
        return int(((linha-1)*(coluna-1))/3)

    def __coordenadas_validas(self, linha, coluna):
        if linha not in range(1,self.__linha):
            print("Linha Invalida")
            return False
        elif coluna not in range(1,self.__coluna):
            print("Coluna Invalida")
            return False
        return True

    def __conta_bombas_vizinho(self, linha, coluna):
        cont = 0
        for l in range(linha-1,linha+2):
            if(l > 0) and (l<= self.__linha):
                for c in range(coluna-1,coluna+2):
                    if(c > 0) and (c <= self.__coluna):
                        posicao = (l,c)
                        if posicao in self.__coordenadas_bombas:
                            cont += 1
                            
        return cont

    """ Funcao para imprimir o tabuleiro na Tela. """
    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            print(str(posicao))

    def __jogada(self, linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina:
                caso sim:
                    Game Over
                caso não:
                    marcar a posição escolhida no tabuleiro com a quantidade de
                    bombas existentes nos nós vizinhos """
        
        if self.__coordenadas_validas(linha,coluna):         
            posicao = (linha,coluna)
            if posicao not in self.__coordenadas_bombas:
                self.__tabuleiro[linha][coluna] = str(self.__conta_bombas_vizinho(linha,coluna))
                return False
            else:
                print("KABOOOM!!! Fim de jogo!!")
                return True

    """ Funcao Principal do Jogo """   
    def principal(self):
        """ Total de Jogadas """
        jogadas = 0 

        """ Variavel de Controle do Loop """
        perdeu = False

        """ Loop principal do Jogo """     
        while not(perdeu):
            unused_variable = os.system("clear")
            self.imprimir_tabuleiro()
            lin = int(input("Digite a linha: "))
            col = int(input("Digite a coluna: "))
            perdeu = self.__jogada(lin,col)
            jogadas = jogadas + 1
            if (((self.__linha-1)*(self.__coluna-1))-jogadas) == int(self.__qtd_bombas):
                print("\nPARABENS!! VOCE VENCEU!!!")
                perdeu = True

        """ Teste para continuar ou sair. """
        flag = str(input("Jogar de novo S/N?"))
        if(flag == 's' or flag == 'S'):
            """ Se Quiser continuar Verdadeiro """
            return True
        else:
            """ Caso contrario Falso """
            return False