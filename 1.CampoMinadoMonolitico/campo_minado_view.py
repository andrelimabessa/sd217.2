from random import randint
from campo_minado_negocio import CampoMinado

linhas = 10
colunas = 10

objeto = CampoMinado(linhas, colunas)
objeto.jogada(
    randint(0, linhas - 1),
    randint(0, colunas - 1)
)
