import sys
from gerenciar_server import servidor
from gerenciar_cliente import cliente

print("Você quer executar:")
print("1 para servidor")
print("2 para cliente")
opcao = input("Opção:")

try:
    if int(opcao) == 1:
        print("Servidor ativado:\n")
        servidor()
    elif int(opcao) == 2:
        print("Cliente ativado:\n")
        cliente()

except : # pega todas possíveis
    for val in sys.exc_info():
        print(val)

input()