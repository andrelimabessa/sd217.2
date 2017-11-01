from random import randint
from os.path import isfile
from os import remove
import json

class CampoMinado:

    def criar_novo_jogo(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__total_jogadas = (linha * coluna) - self.__total_bombas(linha, coluna)
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)
        self.jogadas_restantes = self.qtd_jogadas()

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

    def __total_bombas(self, linha, coluna):
        return int((linha*coluna)/3)

    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            return (str(posicao))

    def tabuleiro_show(self):
        return  self.__tabuleiro

    def _coordenadas_validas(self, linha, coluna):
        if linha not in range(0, self.__linha):
            print("linha invalida")
            return False
        elif coluna not in range(0, self.__coluna):
            print("coluna invalida")
            return False
        return True

    def _conta_bombas_vizinho(self, linha, coluna):
        bombas = 0
        for line in range(linha-1, linha+1):
            for col in range(coluna-1, coluna+1):
                posicao = (line, col)
                if posicao in self.__coordenadas_bombas:
                    bombas += 1
        return str(bombas)

    def _marca_jogada(self, linha, coluna):
        marcador = self._conta_bombas_vizinho(linha, coluna)
        self.__tabuleiro[linha][coluna] = marcador
        #self.imprimir_tabuleiro()

    def proxima_jogada(self):
        return self.__total_jogadas > 0

    def gameOver(self):
         print("______________MINA ACERTADA____________________")
         print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
         print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
         print(". . . . . @ BOOM!!! ÉRROOOUU ! Fastop ! @ . .. . . ")
         print(". . . . @ . . . . . . . . . . . . . . @ . . . .")
         print(". . @ . . . . . . . . . . . . . . . . . . @ . .")
         print("_________________________________________________\n\n")
         remove("game.json")

    def qtd_jogadas(self):
        return self.__total_jogadas

    def jogada(self, linha, coluna):
        if self._coordenadas_validas(linha, coluna):
            posicao = (linha, coluna)
            if posicao in self.__coordenadas_bombas:
                #self.imprimir_tabuleiro()
                self.__total_jogadas = 0
                self.gameOver()
            else:
                self._marca_jogada(linha, coluna)
                self.__total_jogadas -= 1
                #print("Boa Jogada!. Jogadas faltando: " + str(self.__total_jogadas))
                self.__salvar()

                if self.__total_jogadas == 0:
                    print("Você venceu!")
                    remove("game.json")


    def __salvar(self):

        game = {
            'linha': self.__linha,
            'coluna': self.__coluna,
            'total_jogadas': self.__total_jogadas,
            'tabuleiro': self.__tabuleiro,
            'coordenadas_bombas': self.__coordenadas_bombas
        }
        arquivo = open("game.json", 'w')

        arquivo.write(json.dumps(game))
        arquivo.close()

    def restaurar(self, game):
        self.__linha = game['linha']
        self.__coluna = game['coluna']
        self.__total_jogadas = game['total_jogadas']
        self.__tabuleiro = game['tabuleiro']
        self.__coordenadas_bombas = game['coordenadas_bombas']
