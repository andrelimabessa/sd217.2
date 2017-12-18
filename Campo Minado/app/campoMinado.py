from random import randint

class CampoMinado:

    def criarNovoJogo(self, linha, coluna):
        self.__linha = linha
        self.__coluna = coluna
        self.__campo = [["X" for x in range(coluna)] for j in range(linha)]
        self.proxJogadas = self.__totalJogadas()
        self.__localizacaoExplosivos= self.__mapearExplosivos()

    def jogada(self, linha, coluna):

        if not self.__validarJogada(linha, coluna):
            return "Jogada Inválida!!"
        elif self.__localizarExplosivos(linha, coluna):
            return "Fim de Jogo!!"

        self.__guardarJogada(linha, coluna, self.__countExplosivos(linha, coluna))
        self.proxJogadas -=1

        if self.proxJogadas == 0:
            return "Você Ganhou!!"

    
    def proxJogadas(self):
        return self.proxJogadas

    def retornarCampo(self):
        return self.__campo

    def exibirCampo(self):
        for posicao in self.__campo:
            print(str(posicao))


    def __validarJogada(self, linha, coluna):
        if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
            return True
        return False

    def __mapearExplosivos(self):
        qtdExplosivos = self.__totalExplosivo()
        localExplosivos = []
        while qtdExplosivos > 0:
            local = (randint(0, self.__linha - 1), randint(0, self.__coluna - 1))
            if local not in localExplosivos:
                localExplosivos.append(local)
                print("("+str(local[0]+1)+","+ str(local[1]+1)+")")
                qtdExplosivos -= 1
        return localExplosivos

    def __totalExplosivo(self):
        return int((self.__linha * self.__coluna) / 3)

    def __localizarExplosivos(self, linha, coluna):
        return (linha, coluna) in self.__localizacaoExplosivos

    def __countExplosivos(self, linha, coluna):
        linhaAdj = linha - 1
        totalExplosivos = 0
        while linhaAdj <= linha + 1:
            colunaAdj = coluna - 1
            while colunaAdj <= coluna + 1:
                if self.__localizarExplosivos(linhaAdj, colunaAdj):
                    totalExplosivos += 1
                colunaAdj += 1
            linhaAdj += 1
        return totalExplosivos

    def __guardarJogada(self, linha, coluna, qtdExplosivos):
        self.__campo[linha][coluna] = str(qtdExplosivos)

    def __totalJogadas(self):
        return (self.__linha * self.__coluna) - self.__totalExplosivo()
