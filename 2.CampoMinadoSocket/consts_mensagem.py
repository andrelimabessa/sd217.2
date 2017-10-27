""" Esse módulo é responsável por armazenar as constantes utilizadas pelas mensagens trocadas entre cliente e servidor """

#CHAVES
#Define que a mensagem carrega um comando
CODIGO_COMANDO = "codigo_comando"


#Define que a mensagem carrega a resposta à um comando
CODIGO_RESPOSTA = "codigo_resposta_comando"
IMPRIMIR = "tabuleiro"
QTD = "jogadas"
#TABULEIRO = "TABU"

#Chave que aponta para o valor da quantinha de LINHAS e COLUNAS
QUANTIDADE_LINHAS = "quantidade_linhas"
QUANTIDADE_COLUNAS = "quantidade_colunas"

#Chave que aponta para o valor da quantinha de LINHAS e COLUNAS
JOGADA_LINHA = "jogada_linha"
JOGADA_COLUNA = "jogada_coluna"

#Valores para as CHAVESCODIGO_COMANDO
#Caso eu queria criar um novo jogo é necessário informar quantidade de LINHA e COLUNA
COMANDO_CRIAR_NOVO_JOGO = "criar_novo_jogo"
COMANDO_RESTAURAR = "restaurar_jogo"

#Caso eu queira verificar se existe algum jogo pendente, verificar qual o código enviado na RESPOSTA
COMANDO_VERIFICAR_JOGO_PENDENTE = "verificar_jogo_pendente"

#Caso eu queira EFETUAR uma jogada, necessário informar LINHA e COLUNA
COMANDO_EFETUAR_JOGADA="efetuar_jogada"
COMANDO_SHOW = "imprimir"

#Valores para as CHAVESCODIGO_COMANDO
RESPOSTA_SUCESSO = "Comando realizado com sucesso"
RESPOSTA_FALHA = "Comando não pode ser executado"
