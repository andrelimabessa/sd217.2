from random import randint
from ast import literal_eval
import os

class CampoMinado:

    def __init__(self, linha, coluna):
        if(linha != 0 and coluna != 0):
            arq=open('campoMinado.txt','w')
            arq.write('')
            arq.close()
            """ Inicializando campo minado com linha X coluna posicoes """
            self.__linha = linha + 1
            self.__coluna = coluna + 1
            self.__tabuleiro = self.__inicializar_tabuleiro(self.__linha,self.__coluna)
            self.__coordenadas_bombas = self.__distribuir_bombas(self.__linha,self.__coluna)
            self.__qtd_bombas = self.__total_bombas(self.__linha,self.__coluna)
            self.__jogadas=0
        else:
            print("Carregando jogo")
            objeto = self.__carregarJogo()
            dici = {}
            dici=literal_eval(objeto[0])
            print(dici)
            self.__linha=dici['linha']
            self.__coluna=dici['coluna']
            self.__qtd_bombas=dici['totalBombas']
            self.__coordenadas_bombas=dici['coordBombas']
            self.__jogadas=dici['jogadas']
            self.__tabuleiro=literal_eval(objeto[1])

    def __naoHaJogo(self):
            return 3
            
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

    def statisticas(self):
        estatisticas = {}
        estatisticas['totBombas'] = self.__qtd_bombas
        estatisticas['totJogadas'] = self.__jogadas
        estatisticas['linMax'] = self.__linha
        estatisticas['colMax'] = self.__coluna
        return estatisticas

    def retorna_tabuleiro(self):
        return self.__tabuleiro

    def salvarJogo(self):
        status = {}
        status['linha']=self.__linha
        status['coluna']=self.__coluna
        status['totalBombas']=self.__qtd_bombas
        status['coordBombas']=self.__coordenadas_bombas
        status['jogadas']=self.__jogadas
        matriz=[]
        matriz.extend(self.__tabuleiro)
        arq=open('./campoMinado.txt','w')
        arq.writelines(str(status))
        arq.writelines("\n")
        arq.writelines(str(matriz))
        arq.writelines("\n")
        arq.close()
        return 2

    def __carregarJogo(self):
        arq=open('campoMinado.txt','r')
        tmp=arq.readlines()
        arq.close()
        return tmp

    def jogada(self,linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina:
                caso sim:
                    Game Over
                caso não:
                    marcar a posição escolhida no tabuleiro com a quantidade de
                    bombas existentes nos nós vizinhos """
        if (linha != 0 and coluna != 0):
            if self.__coordenadas_validas(linha,coluna):
                posicao = (linha,coluna)
                if posicao not in self.__coordenadas_bombas:
                    self.__tabuleiro[linha][coluna] = str(self.__conta_bombas_vizinho(linha,coluna))
                    self.__jogadas=self.__jogadas+1
                    self.salvarJogo()
                    return False
                else:
                    self.__tabuleiro[linha][coluna] = '*'
                    self.salvarJogo()
                    return True
        else:
            msg=self.salvarJogo()
            return msg

    def total_bombas(self):
        tot_bombas = self.__qtd_bombas;
        return tot_bombas

    def linhaColuna(self):
        dici = {'linha':self.__linha,'coluna':self.__coluna}
        return dici

    def matriz_bomba(self,board):
        taboleiro = []
        taboleiro.extend(board)
        for l in range(1,self.__linha):
            for c in range(1,self.__coluna):
                posicao = (l,c)
                if posicao in self.__coordenadas_bombas:
                    if(taboleiro[l][c] != '*'):
                        taboleiro[l][c] = 'B'
                elif (taboleiro[l][c] == 'X'):
                    taboleiro[l][c] = ' '
                else:
                    pass

        arq=open('campoMinado.txt','w')
        arq.write('1')
        arq.close()
        return taboleiro

    def retornaTabuleiro():
        arq=open('campoMinado.txt','r')
        tmp=arq.readlines()
        arq.close()
        tabuleiro = literal_eval(tmp[1])
        return tabuleiro
        