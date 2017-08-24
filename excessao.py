a = [1, 2, 3]
try:
    print(str(a[5]))
except:
    print("Posição inexistente")
finally:
    print("Fim do teste")
